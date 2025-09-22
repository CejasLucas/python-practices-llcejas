from flask import request
from flask_socketio import emit
from WebApp import socketio
from Modules.__modules__ import menu
import importlib

clients = {}

@socketio.on('start_exercise')
def start_exercise(data):
    file_name = data.get('file_name')
    exercise_id = int(data.get('exercise_id'))

    modulo = next((m for m in menu() if m['file_name'] == file_name), None)
    if not modulo or 'submenu_func' not in modulo:
        emit('output', 'Ejercicio no encontrado\r\n')
        return

    module_path, func_name = modulo['submenu_func'].rsplit('.', 1)
    imported_module = importlib.import_module(module_path)
    submenu_func = getattr(imported_module, func_name)
    exercises = submenu_func()
    exercise = exercises.get(exercise_id)

    if not exercise:
        emit('output', 'Ejercicio inválido\r\n')
        return

    gen = exercise["func"]()
    clients[request.sid] = gen

    try:
        output = next(gen)
        emit('output', output)
    except StopIteration:
        emit('end')

@socketio.on('input')
def handle_input(data):
    sid = request.sid
    gen = clients.get(sid)

    if not gen:
        emit('output', 'No hay ejercicio en ejecución.\r\n')
        return

    try:
        output = gen.send(data.strip())
        emit('output', output)
    except StopIteration:
        emit('end')
        del clients[sid]