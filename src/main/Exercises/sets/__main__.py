from src.main.Modules.sets import get_sets_exercises, get_sets_menu_text
from src.main.Modules.__builder__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_sets_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n============================== COLLECTIONS PRACTICE SET ==============================")

    builder = ExerciseBuilder(exercises=exercises, menu_text=get_sets_menu_text())
    builder.run()