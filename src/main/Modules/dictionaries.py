# WebApp/__utils__/Modules/dictionaries.py
from Exercises.dictionaries.exercise1 import run_exercise_1
from Exercises.dictionaries.exercise2 import run_exercise_2
from Exercises.dictionaries.exercise3 import run_exercise_3

def get_dict_menu_text():
    return (
        "Which example would you like to run?\n"
        "1 - Add contacts (name and phone number) to a dictionary. No duplicate names allowed.\n"
        "2 - Fruit price calculator. Enter fruit name and quantity sold to get the total price.\n"
        "3 - Student grades. Store students and their grades, then calculate average per student.\n"
        "0 - Exit."
    )

def get_dictionaries_exercises():
    return {
        1: {"name": "Add contacts to a dictionary", "func": run_exercise_1},
        2: {"name": "Fruit price calculator", "func": run_exercise_2},
        3: {"name": "Student grades with average", "func": run_exercise_3},
    }
