from src.main.Modules.cycle_for import get_cycle_for_exercises, get_for_menu_text
from src.main.Modules.__builder__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_cycle_for_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n======================= CYCLE FOR PRACTICE =======================" + Style.RESET_ALL)

    builder = ExerciseBuilder(exercises=exercises, menu_text=get_for_menu_text())
    builder.run()