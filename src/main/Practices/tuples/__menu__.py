from .exercise1 import run_exercise_1
from .exercise2 import run_exercise_2
from .exercise3 import run_exercise_3

def get_tuples_exercises():
    return {
        1: {"name": "Count occurrences in a tuple", "func": run_exercise_1},
        2: {"name": "Get value from tuple by index", "func": run_exercise_2},
        3: {"name": "Passenger and destination queries", "func": run_exercise_3},
    }
