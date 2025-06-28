from src.main.__utils__.builder import ExerciseBuilder
from src.main.sets.exercise1 import run_exercise_1
from src.main.sets.exercise2 import run_exercise_2
from src.main.sets.exercise3 import run_exercise_3
from src.main.sets.exercise4 import run_exercise_4
from colorama import Fore, Style

def get_sets_exercises():
    return {
        1: run_exercise_1,
        2: run_exercise_2,
        3: run_exercise_3,
        4: run_exercise_4
    }

def get_sets_menu_text():
    return (
            "Which example would you like to run? \n"
            "1 - Intersection of sets without duplicates.\n"
            "2 - Union of sets without duplicates.\n"
            "3 - Difference of sets without duplicates.\n"
            "4 - Set operations toolkit (union, intersection, difference, equality, deduplication).\n"
            "0 - Exit."
    )

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n============================== COLLECTIONS PRACTICE SET ==============================")
    builder = ExerciseBuilder(exercises=get_sets_exercises(), menu_text=get_sets_menu_text())
    builder.run()