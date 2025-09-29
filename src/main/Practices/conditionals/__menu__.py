from .exercise1 import run_exercise_1
from .exercise2 import run_exercise_2
from .exercise3 import run_exercise_3
from .exercise4 import run_exercise_4
from .exercise5 import run_exercise_5
from .exercise6 import run_exercise_6

def get_conditionals_exercises():
    return {
        1: {"name": "Find the Smaller Number", "func": run_exercise_1},
        2: {"name": "Day of the Week", "func": run_exercise_2},
        3: {"name": "Voting System", "func": run_exercise_3},
        4: {"name": "Check for Vowel", "func": run_exercise_4},
        5: {"name": "Leap Year", "func": run_exercise_5},
        6: {"name": "Students of an Institute", "func": run_exercise_6},
    }
