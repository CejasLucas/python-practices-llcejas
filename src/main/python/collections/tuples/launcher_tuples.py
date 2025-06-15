from src.main.python.collections.tuples.exercise1 import run_exercise_1
from src.main.python.collections.tuples.exercise2 import run_exercise_2
from src.main.python.collections.tuples.exercise3 import run_exercise_3
from colorama import Fore, Style

examples = {
    1: run_exercise_1,
    2: run_exercise_2,
    3: run_exercise_3
}

def run(number): examples[number]()

def menu():
    print(Fore.LIGHTWHITE_EX + Style.DIM + "Which example would you like to run?")
    print("1 - Create a tuple with numbers and show how many times a given number appears")
    print("2 - Display the value from a tuple (1 to 10) based on a given index")
    print("3 - Manage passengers and destinations with queries by ID or country")
    print("0 - Exit")