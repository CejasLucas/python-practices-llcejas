from src.main.__utils__.builder import ExerciseBuilder
from src.main.utils_numpy.exercise1 import run_exercise_1
from src.main.utils_numpy.exercise2 import run_exercise_2
from src.main.utils_numpy.exercise3 import run_exercise_3
from src.main.utils_numpy.exercise4 import run_exercise_4
from colorama import Fore, Style

def get_numpy_exercises():
    return {
        1: run_exercise_1,
        2: run_exercise_2,
        3: run_exercise_3,
        4: run_exercise_4
    }

def get_numpy_menu_text():
    return (
        "Which NumPy exercise would you like to run?\n"
        "1 - Matrix operations (subtraction, multiplication, slicing, printing last row).\n"
        "2 - Matrix element sum and average (using loops and NumPy).\n"
        "3 - Create a 7x9 matrix with specific column values and compute the average of the last row.\n"
        "4 - Create a 5x5 random matrix and print positions of elements > 0.5.\n"
        "0 - Exit."
    )

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n=========================== NUMPY PRACTICE MENU ===========================")
    builder = ExerciseBuilder(exercises=get_numpy_exercises(), menu_text=get_numpy_menu_text())
    builder.run()