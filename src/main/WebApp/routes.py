from flask import Blueprint, render_template, abort
from werkzeug.utils import send_file

from Modules.__modules__ import menu
import importlib, os, tempfile

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def main_menu():
    return render_template('menu.html', modulos=menu())

@main_bp.route('/module/<file_name>')
def module_page(file_name):
    modulo = next((m for m in menu() if m['file_name'] == file_name), None)
    if not modulo: abort(404)

    submenu = []
    if 'submenu_func' in modulo:
        module_path, func_name = modulo['submenu_func'].rsplit('.', 1)
        imported_module = importlib.import_module(module_path)
        submenu_func = getattr(imported_module, func_name)
        exercises = submenu_func()
        submenu = [{"id": int(k), "name": v["name"]} for k,v in exercises.items()]

    return render_template('module.html', modulo=modulo, submenu=submenu)

@main_bp.route('/module/<file_name>/exercise/<int:exercise_id>')
def run_exercise(file_name, exercise_id):
    modulo = next((m for m in menu() if m['file_name'] == file_name), None)
    if not modulo or 'submenu_func' not in modulo: abort(404)

    return render_template(
        'terminal.html',
        file_name=file_name,
        exercise_id=exercise_id,
        modulo=modulo
    )

@main_bp.route('/plot/<plot_id>.png')
def get_plot(plot_id):
    filepath = os.path.join(tempfile.gettempdir(), 'plots', f'{plot_id}.png')
    if not os.path.exists(filepath): return abort(404)
    return send_file(filepath, mimetype='image/png')
