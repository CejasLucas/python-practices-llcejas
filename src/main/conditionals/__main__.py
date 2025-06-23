from src.main.__utils__.builder import ExerciseBuilder
from src.main.conditionals.exercise1 import run_exercise_1
from src.main.conditionals.exercise2 import run_exercise_2
from src.main.conditionals.exercise3 import run_exercise_3
from src.main.conditionals.exercise4 import run_exercise_4
from src.main.conditionals.exercise5 import run_exercise_5
from src.main.conditionals.exercise6 import run_exercise_6
from colorama import Fore, Style

def get_conditionals_exercises():
    return {
        1: run_exercise_1,
        2: run_exercise_2,
        3: run_exercise_3,
        4: run_exercise_4,
        5: run_exercise_5,
        6: run_exercise_6
    }

def get_conditionals_menu_text():
    return (
            Fore.LIGHTWHITE_EX + Style.DIM +
            "Which example do you want to run?.\n"
            "1 - Find the Smaller Number.\n"
            "2 - Day of the Week.\n"
            "3 - Voting System.\n"
            "4 - Check for Vowel.\n"
            "5 - Leap Year.\n"
            "6 - Students of an institute.\n"
            "0 - Exit."
    )

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + "\n=======CONDITIONALS PRACTICE=======")
    builder = ExerciseBuilder(exercises=get_conditionals_exercises(), menu_text=get_conditionals_menu_text())
    builder.run()