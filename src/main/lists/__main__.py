from src.main.__utils__.builder import ExerciseBuilder
from src.main.lists.exercise1 import run_exercise_1
from src.main.lists.exercise2 import run_exercise_2
from src.main.lists.exercise3 import run_exercise_3
from src.main.lists.exercise4 import run_exercise_4
from src.main.lists.exercise5 import run_exercise_5
from src.main.lists.exercise6 import run_exercise_6
from colorama import Fore, Style

def get_lists_exercises():
    return {
        1: run_exercise_1,
        2: run_exercise_2,
        3: run_exercise_3,
        4: run_exercise_4,
        5: run_exercise_5,
        6: run_exercise_6
    }

def get_lists_menu_text():
    return (
            "Which example would you like to run?\n"
            "1 - Create a list of words and display it.\n"
            "2 - Count how many times a word appears in the list.\n"
            "3 - Replace a word in the list with another.\n"
            "4 - Remove a word from the list.\n"
            "5 - Remove from the first list the words that appear in the second list.\n"
            "6 - Create a reversed copy of the list.\n"
            "0 - Exit."
    )

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n=========================== COLLECTIONS PRACTICE LIST ===========================")
    builder = ExerciseBuilder(exercises=get_lists_exercises(), menu_text=get_lists_menu_text())
    builder.run()