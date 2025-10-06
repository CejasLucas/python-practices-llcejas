from .exercise1 import run_exercise_1
from .exercise2 import run_exercise_2
from .exercise3 import run_exercise_3
from .exercise4 import run_exercise_4

def get_sets_exercises():
    return {
        1: {"name": "Intersection of sets", "func": run_exercise_1},
        2: {"name": "Union of sets", "func": run_exercise_2},
        3: {"name": "Difference of sets", "func": run_exercise_3},
        4: {"name": "Set operations toolkit", "func": run_exercise_4},
    }
