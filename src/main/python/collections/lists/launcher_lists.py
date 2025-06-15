from src.main.python.collections.lists.exercise1 import run_exercise_1
from src.main.python.collections.lists.exercise2 import run_exercise_2
from src.main.python.collections.lists.exercise3 import run_exercise_3
from src.main.python.collections.lists.exercise4 import run_exercise_4
from src.main.python.collections.lists.exercise5 import run_exercise_5
from src.main.python.collections.lists.exercise6 import run_exercise_6
from colorama import Fore, Style

exercises = {
    1: run_exercise_1,
    2: run_exercise_2,
    3: run_exercise_3,
    4: run_exercise_4,
    5: run_exercise_5,
    6: run_exercise_6
}

def run(number): exercises[number]()

def menu():
    print(Fore.LIGHTWHITE_EX + Style.DIM + "Which example would you like to run?")
    print("1 - Create a list of words and display it")
    print("2 - Count how many times a word appears in the list")
    print("3 - Replace a word in the list with another")
    print("4 - Remove a word from the list")
    print("5 - Remove from the first list the words that appear in the second list")
    print("6 - Create a reversed copy of the list")
    print("0 - Exit")