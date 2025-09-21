# WebApp/__utils__/Modules/lists.py
from Exercises.lists.exercise1 import run_exercise_1
from Exercises.lists.exercise2 import run_exercise_2
from Exercises.lists.exercise3 import run_exercise_3
from Exercises.lists.exercise4 import run_exercise_4
from Exercises.lists.exercise5 import run_exercise_5
from Exercises.lists.exercise6 import run_exercise_6

def get_lists_menu_text():
    return (
        "Which example would you like to run?\n"
        "1 - Create a list of words and display it.\n"
        "2 - Count how many times a word appears in the list.\n"
        "3 - Replace a word in the list with another.\n"
        "4 - Remove a word from the list.\n"
        "5 - Remove from the first list the words that appear in the second list.\n"
        "6 - Create a reversed copy of the list.\n"
        "0 - Exit."
    )

def get_lists_exercises():
    return {
        1: {"name": "Create a list of words and display it", "func": run_exercise_1},
        2: {"name": "Count how many times a word appears", "func": run_exercise_2},
        3: {"name": "Replace a word in the list", "func": run_exercise_3},
        4: {"name": "Remove a word from the list", "func": run_exercise_4},
        5: {"name": "Remove from list1 words in list2", "func": run_exercise_5},
        6: {"name": "Create a reversed copy of the list", "func": run_exercise_6},
    }
