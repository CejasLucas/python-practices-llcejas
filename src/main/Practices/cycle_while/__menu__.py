from .exercise1 import run_exercise_1
from .exercise2 import run_exercise_2
from .exercise3 import run_exercise_3
from .exercise4 import run_exercise_4
from .exercise5 import run_exercise_5
from .exercise6 import run_exercise_6
from .exercise7 import run_exercise_7
from .exercise8 import run_exercise_8

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
