from .exercise1 import run_exercise_1
from .exercise2 import run_exercise_2
from .exercise3 import run_exercise_3
from .exercise4 import run_exercise_4
from .exercise5 import run_exercise_5
from .exercise6 import run_exercise_6

def get_lists_exercises():
    return {
        1: {"name": "Create a list of words and display it", "func": run_exercise_1},
        2: {"name": "Count how many times a word appears", "func": run_exercise_2},
        3: {"name": "Replace a word in the list", "func": run_exercise_3},
        4: {"name": "Remove a word from the list", "func": run_exercise_4},
        5: {"name": "Remove from list1 words in list2", "func": run_exercise_5},
        6: {"name": "Create a reversed copy of the list", "func": run_exercise_6},
    }
