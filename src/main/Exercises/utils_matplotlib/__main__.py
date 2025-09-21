from src.main.Modules.utils_matplotlib import get_matplotlib_menu_text, get_matplotlib_exercises
from src.main.Modules.__builder__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_matplotlib_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n=========================== MATPLOTLIB PRACTICE MENU ===========================")

    builder = ExerciseBuilder(exercises=exercises, menu_text=get_matplotlib_menu_text())
    builder.run()