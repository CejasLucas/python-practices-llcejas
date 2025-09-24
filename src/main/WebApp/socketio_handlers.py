from flask import request
from flask_socketio import emit
from WebApp import socketio
from Modules.__modules__ import menu
import importlib
import builtins

clients = {}

def exercise_runner(func):
    output_buffer = []
    waiting_for_input = [None]

    real_input = builtins.input
    real_print = builtins.print

    # Redirigir print
    builtins.print = lambda *args, **kwargs: output_buffer.append(" ".join(map(str, args)) + "\n")

    # Redirigir input
    def mock_input(prompt=""):
        if prompt:
            output_buffer.append(prompt)
        # Primero enviamos cualquier output pendiente
        if output_buffer:
            out = "".join(output_buffer)
            output_buffer.clear()
            val = yield out  # yield el prompt al frontend
        else:
            val = yield
        # Esperamos a que el cliente mande input
        waiting_for_input[0] = None
        while waiting_for_input[0] is None:
            waiting_for_input[0] = (yield)
        return waiting_for_input[0]

    builtins.input = lambda prompt="": (yield from mock_input(prompt))

    try:
        func()
        if output_buffer:
            yield "".join(output_buffer)
    finally:
        builtins.input = real_input
        builtins.print = real_print


@socketio.on("start_exercise")
def start_exercise(data):
    file_name = data.get("file_name")
    exercise_id = int(data.get("exercise_id"))

    modulo = next((m for m in menu() if m["file_name"] == file_name), None)
    if not modulo or "submenu_func" not in modulo:
        emit("output", "Ejercicio no encontrado\r\n")
        return

    module_path, func_name = modulo["submenu_func"].rsplit(".", 1)
    imported_module = importlib.import_module(module_path)
    submenu_func = getattr(imported_module, func_name)
    exercises = submenu_func()
    exercise = exercises.get(exercise_id)

    if not exercise:
        emit("output", "Ejercicio inválido\r\n")
        return

    # Inicializamos cliente
    clients[request.sid] = {"input_ready": False, "input_value": None}

    # Creamos generador
    gen = exercise_runner(exercise["func"])
    clients[request.sid]["gen"] = gen

    # Ejecutamos primer yield (prints iniciales o prompt)
    try:
        output = next(gen)
        if output:
            emit("output", output)
    except StopIteration:
        emit("end")
        del clients[request.sid]

@socketio.on("input")
def handle_input(data):
    sid = request.sid
    client = clients.get(sid)
    if not client or "gen" not in client:
        emit("output", "No hay ejercicio en ejecución.\r\n")
        return

    # Guardamos input del usuario
    client["input_value"] = data.strip()
    client["input_ready"] = True

    try:
        output = next(client["gen"])
        if output:
            emit("output", output)
    except StopIteration:
        emit("end")
        del clients[sid]