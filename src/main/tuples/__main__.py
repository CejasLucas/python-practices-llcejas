from src.main.__utils__.builder import ExerciseBuilder
from src.main.tuples.exercise1 import run_exercise_1
from src.main.tuples.exercise2 import run_exercise_2
from src.main.tuples.exercise3 import run_exercise_3
from colorama import Fore, Style

def get_tuples_exercises():
    return {
        1: run_exercise_1,
        2: run_exercise_2,
        3: run_exercise_3
    }

def get_tuples_menu_text():
    return (
        "Which example would you like to run?\n"
        "1 - Create a tuple with numbers and show how many times a given number appears.\n"
        "2 - Display the value from a tuple (1 to 10) based on a given index.\n"
        "3 - Manage passengers and destinations with queries by ID or country.\n"
        "0 - Exit."
    )

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n============================== COLLECTIONS PRACTICE TUPLE ==============================")
    builder = ExerciseBuilder(exercises=get_tuples_exercises(), menu_text=get_tuples_menu_text())
    builder.run()