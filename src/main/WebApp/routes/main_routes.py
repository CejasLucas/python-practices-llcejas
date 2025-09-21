from flask import Blueprint, render_template, abort
from Modules.__modules__ import menu
import importlib

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def main_menu():
    return render_template('main.html', modulos=menu())

@main_bp.route('/module/<file_name>')
def module_page(file_name):
    modulo = next((m for m in menu() if m['file_name'] == file_name), None)
    if not modulo:
        abort(404)

    submenu = []
    if 'submenu_func' in modulo:
        module_path, func_name = modulo['submenu_func'].rsplit('.', 1)
        imported_module = importlib.import_module(module_path)
        submenu_func = getattr(imported_module, func_name)
        exercises = submenu_func()
        submenu = [{"id": k, "name": v["name"]} for k, v in exercises.items()]

    return render_template('module.html', modulo=modulo, submenu=submenu)

@main_bp.route('/module/<file_name>/exercise/<int:exercise_id>')
def run_exercise(file_name, exercise_id):
    modulo = next((m for m in menu() if m['file_name'] == file_name), None)
    if not modulo or 'submenu_func' not in modulo:
        abort(404)

    module_path, func_name = modulo['submenu_func'].rsplit('.', 1)
    imported_module = importlib.import_module(module_path)
    submenu_func = getattr(imported_module, func_name)
    exercises = submenu_func()

    exercise = exercises.get(exercise_id)
    if not exercise:
        abort(404)

    try:
        result = exercise["func"]()
    except Exception as e:
        result = f"Error al ejecutar el ejercicio: {str(e)}"

    return render_template('exercise.html', modulo=modulo, exercise_id=exercise_id, result=result)
