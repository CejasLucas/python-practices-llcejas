# WebApp/modules/submodules/conditionals.py
from src.main.conditionals.exercise1 import run_exercise_1
from src.main.conditionals.exercise2 import run_exercise_2
from src.main.conditionals.exercise3 import run_exercise_3
from src.main.conditionals.exercise4 import run_exercise_4
from src.main.conditionals.exercise5 import run_exercise_5
from src.main.conditionals.exercise6 import run_exercise_6

def get_conditionals_menu_text():
    return (
        "Which example do you want to run?.\n"
        "1 - Find the Smaller Number.\n"
        "2 - Day of the Week.\n"
        "3 - Voting System.\n"
        "4 - Check for Vowel.\n"
        "5 - Leap Year.\n"
        "6 - Students of an institute.\n"
        "0 - Exit."
    )

def get_conditionals_exercises():
    return {
        1: {"name": "Find the Smaller Number", "func": run_exercise_1},
        2: {"name": "Day of the Week", "func": run_exercise_2},
        3: {"name": "Voting System", "func": run_exercise_3},
        4: {"name": "Check for Vowel", "func": run_exercise_4},
        5: {"name": "Leap Year", "func": run_exercise_5},
        6: {"name": "Students of an Institute", "func": run_exercise_6}
    }
