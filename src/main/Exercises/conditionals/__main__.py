from Modules.conditionals import get_conditionals_menu_text, get_conditionals_exercises
from Modules.__builder__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_conditionals_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n========== CONDITIONALS PRACTICE ==========")

    builder = ExerciseBuilder(exercises=exercises, menu_text=get_conditionals_menu_text())
    builder.run()