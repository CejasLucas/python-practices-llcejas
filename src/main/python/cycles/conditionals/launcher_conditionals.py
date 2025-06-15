from src.main.python.cycles.conditionals.exercise1 import run_exercise_1
from src.main.python.cycles.conditionals.exercise2 import run_exercise_2
from src.main.python.cycles.conditionals.exercise3 import run_exercise_3
from src.main.python.cycles.conditionals.exercise4 import run_exercise_4
from src.main.python.cycles.conditionals.exercise5 import run_exercise_5
from src.main.python.cycles.conditionals.exercise6 import run_exercise_6
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
    print(Fore.LIGHTWHITE_EX + Style.DIM +"Which example do you want to run?")
    print("1 - Find the Smaller Number")
    print("2 - Day of the Week")
    print("3 - Voting System")
    print("4 - Check for Vowel")
    print("5 - Leap Year")
    print("6 - Students of an institute")
    print("0 - Exit")