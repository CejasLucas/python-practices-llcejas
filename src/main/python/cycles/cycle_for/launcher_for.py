from src.main.python.cycles.cycle_for.exercise1 import run_exercise_1
from src.main.python.cycles.cycle_for.exercise2 import run_exercise_2
from src.main.python.cycles.cycle_for.exercise3 import run_exercise_3
from src.main.python.cycles.cycle_for.exercise4 import run_exercise_4
from colorama import Fore, Style

exercises = {
    1: run_exercise_1,
    2: run_exercise_2,
    3: run_exercise_3,
    4: run_exercise_4
}

def run(number): exercises[number]()

def menu():
    print(Fore.LIGHTWHITE_EX + Style.DIM + "Which exercise would you like to run?")
    print("1 - Print the first 100 natural numbers")
    print("2 - Sum the first N odd numbers")
    print("3 - Calculate the factorial of a number")
    print("4 - Display the first N numbers of the Fibonacci sequence")
    print("0 - Exit")