from src.main.Modules.__builder__ import ExerciseBuilder
from src.main.Modules.utils_pandas import get_pandas_exercises, get_pandas_menu_text
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_pandas_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n=========================== PANDAS PRACTICE MENU ===========================")

    builder = ExerciseBuilder(exercises=exercises, menu_text=get_pandas_menu_text())
    builder.run()