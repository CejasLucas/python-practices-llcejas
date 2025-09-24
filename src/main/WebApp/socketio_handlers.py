import sys
import io
import queue
import importlib
import builtins
import threading

from flask import request
from WebApp import socketio
from flask_socketio import emit
from Modules.__modules__ import menu

clients = {}

def run_exercise(func, sid, input_queue, output_queue):
    real_input = builtins.input
    real_print = builtins.print
    real_stdout = sys.stdout

    sys.stdout = io.StringIO()

    def fake_input(prompt=""):
        if prompt:
            print(prompt, end="")
        output_queue.put(sys.stdout.getvalue())
        sys.stdout.seek(0)
        sys.stdout.truncate(0)
        return input_queue.get()

    builtins.input = fake_input
    builtins.print = lambda *args, **kwargs: real_print(*args, file=sys.stdout, **kwargs)

    try:
        func()
        output_queue.put(sys.stdout.getvalue())
    except Exception as e:
        output_queue.put(f"[ERROR] {e}\n")
    finally:
        builtins.input = real_input
        builtins.print = real_print
        sys.stdout = real_stdout
        output_queue.put(None)


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

    sid = request.sid
    input_queue = queue.Queue()
    output_queue = queue.Queue()
    clients[sid] = {"input_queue": input_queue, "output_queue": output_queue}

    # hilo que ejecuta el ejercicio
    threading.Thread(
        target=run_exercise,
        args=(exercise["func"], sid, input_queue, output_queue),
        daemon=True
    ).start()

    # hilo que manda output al cliente
    def streamer():
        while True:
            msg = output_queue.get()
            if msg is None:
                socketio.emit("end", room=sid)
                break
            if msg:
                socketio.emit("output", msg, room=sid)

    threading.Thread(target=streamer, daemon=True).start()


@socketio.on("input")
def handle_input(data):
    sid = request.sid
    client = clients.get(sid)
    if not client:
        emit("output", "No hay ejercicio en ejecución.\r\n")
        return
    client["input_queue"].put(data.strip())
