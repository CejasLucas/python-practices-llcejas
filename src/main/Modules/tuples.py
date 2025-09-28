# WebApp/__utils__/Modules/tuples.py
from Practices.tuples.exercise1 import run_exercise_1
from Practices.tuples.exercise2 import run_exercise_2
from Practices.tuples.exercise3 import run_exercise_3

def get_tuples_menu_text():
    return (
        "Which example would you like to run?\n"
        "1 - Create a tuple with numbers and show how many times a given number appears.\n"
        "2 - Display the value from a tuple (1 to 10) based on a given index.\n"
        "3 - Manage passengers and destinations with queries by ID or country.\n"
        "0 - Exit."
    )

def get_tuples_exercises():
    return {
        1: {"name": "Count occurrences in a tuple", "func": run_exercise_1},
        2: {"name": "Get value from tuple by index", "func": run_exercise_2},
        3: {"name": "Passenger and destination queries", "func": run_exercise_3},
    }
