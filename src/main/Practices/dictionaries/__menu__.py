from .exercise1 import run_exercise_1
from .exercise2 import run_exercise_2
from .exercise3 import run_exercise_3

def get_dictionaries_exercises():
    return {
        1: {"name": "Add contacts to a dictionary", "func": run_exercise_1},
        2: {"name": "Fruit price calculator", "func": run_exercise_2},
        3: {"name": "Student grades with average", "func": run_exercise_3},
    }
