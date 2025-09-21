# WebApp/__utils__/Modules/sets.py
from Exercises.sets.exercise1 import run_exercise_1
from Exercises.sets.exercise2 import run_exercise_2
from Exercises.sets.exercise3 import run_exercise_3
from Exercises.sets.exercise4 import run_exercise_4

def get_sets_menu_text():
    return (
        "Which example would you like to run?\n"
        "1 - Intersection of sets without duplicates.\n"
        "2 - Union of sets without duplicates.\n"
        "3 - Difference of sets without duplicates.\n"
        "4 - Set operations toolkit (union, intersection, difference, equality, deduplication).\n"
        "0 - Exit."
    )

def get_sets_exercises():
    return {
        1: {"name": "Intersection of sets", "func": run_exercise_1},
        2: {"name": "Union of sets", "func": run_exercise_2},
        3: {"name": "Difference of sets", "func": run_exercise_3},
        4: {"name": "Set operations toolkit", "func": run_exercise_4},
    }
