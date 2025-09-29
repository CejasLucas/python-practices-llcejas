from .exercise1 import run_exercise_1
from .exercise2 import run_exercise_2
from .exercise3 import run_exercise_3
from .exercise4 import run_exercise_4

def get_cycle_for_exercises():
    return {
        1: {"name": "Print the first 100 natural numbers", "func": run_exercise_1},
        2: {"name": "Sum the first N odd numbers", "func": run_exercise_2},
        3: {"name": "Calculate the factorial of a number", "func": run_exercise_3},
        4: {"name": "Display the first N numbers of the Fibonacci sequence", "func": run_exercise_4},
    }
