from src.main.Modules.utils_networkx import get_networkx_exercises, get_networkx_menu_text
from src.main.Modules.__builder__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_networkx_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n=========================== PRÁCTICA NETWORKX Y GRAFOS ===========================")

    builder = ExerciseBuilder(exercises=exercises, menu_text=get_networkx_menu_text())
    builder.run()