from src.main.Modules.tuples import get_tuples_exercises, get_tuples_menu_text
from src.main.Modules.__builder__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_tuples_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n============================== COLLECTIONS PRACTICE TUPLE ==============================")

    builder = ExerciseBuilder(exercises=exercises, menu_text=get_tuples_menu_text())
    builder.run()