# WebApp/__utils__/Modules/cycle_while.py
from Exercises.cycle_while.exercise1 import run_exercise_1
from Exercises.cycle_while.exercise2 import run_exercise_2
from Exercises.cycle_while.exercise3 import run_exercise_3
from Exercises.cycle_while.exercise4 import run_exercise_4
from Exercises.cycle_while.exercise5 import run_exercise_5
from Exercises.cycle_while.exercise6 import run_exercise_6
from Exercises.cycle_while.exercise7 import run_exercise_7
from Exercises.cycle_while.exercise8 import run_exercise_8

def get_while_menu_text():
    return (
        "Which example do you want to run?\n"
        "1 - Enter a specified amount of positive numbers.\n"
        "2 - Enter a second number greater than the first.\n"
        "3 - Keep entering decimals greater than the first.\n"
        "4 - Keep entering increasingly larger integers.\n"
        "5 - Enter numbers until a negative is entered, then sum them.\n"
        "6 - Enter numbers until their sum exceeds a given limit.\n"
        "7 - Enter numbers between two values until one is outside the range.\n"
        "8 - Enter even numbers while choosing to continue.\n"
        "0 - Exit."
    )

def get_cycle_while_exercises():
    return {
        1: {"name": "Enter a specified amount of positive numbers", "func": run_exercise_1},
        2: {"name": "Enter a second number greater than the first", "func": run_exercise_2},
        3: {"name": "Keep entering decimals greater than the first", "func": run_exercise_3},
        4: {"name": "Keep entering increasingly larger integers", "func": run_exercise_4},
        5: {"name": "Enter numbers until a negative is entered, then sum them", "func": run_exercise_5},
        6: {"name": "Enter numbers until their sum exceeds a given limit", "func": run_exercise_6},
        7: {"name": "Enter numbers between two values until one is outside the range", "func": run_exercise_7},
        8: {"name": "Enter even numbers while choosing to continue", "func": run_exercise_8},
    }
