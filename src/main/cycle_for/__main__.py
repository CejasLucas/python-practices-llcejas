from src.main.__utils__.builder import ExerciseBuilder
from src.main.cycle_for.exercise1 import run_exercise_1
from src.main.cycle_for.exercise2 import run_exercise_2
from src.main.cycle_for.exercise3 import run_exercise_3
from src.main.cycle_for.exercise4 import run_exercise_4
from colorama import Fore, Style

def get_for_exercises():
    return {
        1: run_exercise_1,
        2: run_exercise_2,
        3: run_exercise_3,
        4: run_exercise_4
    }

def get_for_menu_text():
    return (
            "Which exercise would you like to run?\n"
            "1 - Print the first 100 natural numbers.\n"
            "2 - Sum the first N odd numbers\n"
            "3 - Calculate the factorial of a number\n"
            "4 - Display the first N numbers of the Fibonacci sequence\n"
            "0 - Exit"
    )

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n======================= CYCLE FOR PRACTICE =======================" + Style.RESET_ALL)
    builder = ExerciseBuilder(exercises=get_for_exercises(), menu_text=get_for_menu_text())
    builder.run()