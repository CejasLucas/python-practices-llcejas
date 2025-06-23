from src.main.__utils__.builder import ExerciseBuilder
from src.main.dictionaries.exercise1 import run_exercise_1
from src.main.dictionaries.exercise2 import run_exercise_2
from src.main.dictionaries.exercise3 import run_exercise_3
from colorama import Fore, Style

def get_dict_exercises():
    return {
        1: run_exercise_1,
        2: run_exercise_2,
        3: run_exercise_3
    }

def get_dict_menu_text():
    return (
        Fore.LIGHTWHITE_EX + Style.DIM +
        "Which example would you like to run?\n"
        "1 - Add contacts (name and phone number) to a dictionary. No duplicate names allowed.\n"
        "2 - Fruit price calculator. Enter fruit name and quantity sold to get the total price.\n"
        "3 - Student grades. Store students and their grades, then calculate average per student.\n"
        "0 - Exit."
    )

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + "\n================================== COLLECTIONS PRACTICE: DICTIONARIES ==================================")
    builder = ExerciseBuilder(exercises=get_dict_exercises(), menu_text=get_dict_menu_text())
    builder.run()