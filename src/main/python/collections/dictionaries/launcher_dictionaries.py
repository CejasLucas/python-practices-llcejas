from src.main.python.collections.dictionaries.exercise1 import run_exercise_1
from src.main.python.collections.dictionaries.exercise2 import run_exercise_2
from src.main.python.collections.dictionaries.exercise3 import run_exercise_3
from colorama import Fore, Style

exercises = {
    1: run_exercise_1,
    2: run_exercise_2,
    3: run_exercise_3
}

def run(number): exercises[number]()

def menu():
    print(Fore.LIGHTWHITE_EX + Style.DIM + "Which example would you like to run?")
    print("1 - Add contacts (name and phone number) to a dictionary. No duplicate names allowed.")
    print("2 - Fruit price calculator: enter fruit name and quantity sold to get the total price.")
    print("3 - Student grades - Store students and their grades, then calculate average per student.")
    print("0 - Exit")
