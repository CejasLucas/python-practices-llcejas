from src.main.python.collections.sets.exercise1 import run_exercise_1
from src.main.python.collections.sets.exercise2 import run_exercise_2
from src.main.python.collections.sets.exercise3 import run_exercise_3
from src.main.python.collections.sets.exercise4 import run_exercise_4
from colorama import Fore, Style

examples = {
    1: run_exercise_1,
    2: run_exercise_2,
    3: run_exercise_3,
    4: run_exercise_4
}

def run(number): examples[number]()

def menu():
    print(Fore.LIGHTWHITE_EX + Style.DIM + "Which example would you like to run?")
    print("1 - Intersection of sets without duplicates")
    print("2 - Union of sets without duplicates")
    print("3 - Difference of sets without duplicates")
    print("4 - Set operations toolkit (union, intersection, difference, equality, deduplication)")
    print("0 - Exit")