from src.main.__utils__.builder import ExerciseBuilder
from src.main.cycle_while.exercise1 import run_exercise_1
from src.main.cycle_while.exercise2 import run_exercise_2
from src.main.cycle_while.exercise3 import run_exercise_3
from src.main.cycle_while.exercise4 import run_exercise_4
from src.main.cycle_while.exercise5 import run_exercise_5
from src.main.cycle_while.exercise6 import run_exercise_6
from src.main.cycle_while.exercise7 import run_exercise_7
from src.main.cycle_while.exercise8 import run_exercise_8
from colorama import Fore, Style

def get_while_exercises():
    return {
        1: run_exercise_1,
        2: run_exercise_2,
        3: run_exercise_3,
        4: run_exercise_4,
        5: run_exercise_5,
        6: run_exercise_6,
        7: run_exercise_7,
        8: run_exercise_8
    }

def get_while_menu_text():
    return (
            Fore.LIGHTWHITE_EX + Style.DIM +
            "Which exercise would you like to run?\n"
            "1 - Enter a specified amount of positive numbers.\n"
            "2 - Enter a second number greater than the first.\n"
            "3 - Keep entering decimals greater than the first.\n"
            "4 - Keep entering increasingly larger integers.\n"
            "5 - Enter numbers until a negative is entered, then sum them.\n"
            "6 - Enter numbers until their sum exceeds a given limit.\n"
            "7 - Enter numbers between two values until one is outside the range.\n"
            "8 - Enter even numbers while choosing to continue.\n"
            "0 - Exit."
    )

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + "\n========================= WHILE CYCLE PRACTICE =========================" + Style.RESET_ALL)
    builder = ExerciseBuilder(exercises=get_while_exercises(), menu_text=get_while_menu_text())
    builder.run()