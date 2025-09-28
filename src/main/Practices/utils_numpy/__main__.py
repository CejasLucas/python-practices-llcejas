from src.main.Modules.utils_numpy import get_numpy_exercises, get_numpy_menu_text
from src.main.Modules.__builder__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_numpy_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n=========================== NUMPY PRACTICE MENU ===========================")

    builder = ExerciseBuilder(exercises=exercises, menu_text=get_numpy_menu_text())
    builder.run()