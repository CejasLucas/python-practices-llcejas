# WebApp/modules/submodules/cycle_for.py
from src.main.cycle_for.exercise1 import run_exercise_1
from src.main.cycle_for.exercise2 import run_exercise_2
from src.main.cycle_for.exercise3 import run_exercise_3
from src.main.cycle_for.exercise4 import run_exercise_4

def get_for_menu_text():
    return (
        "Which example do you want to run?\n"
        "1 - Print the first 100 natural numbers.\n"
        "2 - Sum the first N odd numbers.\n"
        "3 - Calculate the factorial of a number.\n"
        "4 - Display the first N numbers of the Fibonacci sequence.\n"
        "0 - Exit."
    )

def get_cycle_for_exercises():
    return {
        1: {"name": "Print the first 100 natural numbers", "func": run_exercise_1},
        2: {"name": "Sum the first N odd numbers", "func": run_exercise_2},
        3: {"name": "Calculate the factorial of a number", "func": run_exercise_3},
        4: {"name": "Display the first N numbers of the Fibonacci sequence", "func": run_exercise_4},
    }
