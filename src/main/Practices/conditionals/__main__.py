from colorama import Fore, Style
from src.main.Practices.__loader__ import ExerciseBuilder
from src.main.Practices.conditionals.__menu__ import get_conditionals_exercises

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_conditionals_exercises().items()}
    submenu = {k: v["name"] for k, v in get_conditionals_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n========== CONDITIONALS PRACTICE ==========")

    builder = ExerciseBuilder(exercises=exercises, menu=submenu)
    builder.run()