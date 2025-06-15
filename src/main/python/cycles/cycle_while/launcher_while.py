from src.main.python.cycles.cycle_while.exercise1 import run_exercise_1
from src.main.python.cycles.cycle_while.exercise2 import run_exercise_2
from src.main.python.cycles.cycle_while.exercise3 import run_exercise_3
from src.main.python.cycles.cycle_while.exercise4 import run_exercise_4
from src.main.python.cycles.cycle_while.exercise5 import run_exercise_5
from src.main.python.cycles.cycle_while.exercise6 import run_exercise_6
from src.main.python.cycles.cycle_while.exercise7 import run_exercise_7
from src.main.python.cycles.cycle_while.exercise8 import run_exercise_8
from colorama import Fore, Style

exercises = {
    1: run_exercise_1,
    2: run_exercise_2,
    3: run_exercise_3,
    4: run_exercise_4,
    5: run_exercise_5,
    6: run_exercise_6,
    7: run_exercise_7,
    8: run_exercise_8
}

def run(number): exercises[number]()

def menu():
    print(Fore.LIGHTWHITE_EX + Style.DIM + "Which exercise would you like to run?")
    print("1 - Enter a specified amount of positive numbers")
    print("2 - Enter a second number greater than the first")
    print("3 - Keep entering decimals greater than the first")
    print("4 - Keep entering increasingly larger integers")
    print("5 - Enter numbers until a negative is entered, then sum them")
    print("6 - Enter numbers until their sum exceeds a given limit")
    print("7 - Enter numbers between two values until one is outside the range")
    print("8 - Enter even numbers while choosing to continue")
    print("0 - Exit")