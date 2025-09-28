from src.main.Modules.cycle_while import get_cycle_while_exercises, get_while_menu_text
from src.main.Modules.__builder__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_cycle_while_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n========================= WHILE CYCLE PRACTICE =========================" + Style.RESET_ALL)

    builder = ExerciseBuilder(exercises=exercises, menu_text=get_while_menu_text())
    builder.run()