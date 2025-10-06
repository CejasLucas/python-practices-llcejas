from src.main.Practices.cycle_for.__menu__ import get_cycle_for_exercises
from src.main.Practices.__loader__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_cycle_for_exercises().items()}
    submenu = {k: v["name"] for k, v in get_cycle_for_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n======================= CYCLE FOR PRACTICE =======================" + Style.RESET_ALL)

    builder = ExerciseBuilder(exercises=exercises, menu=submenu)
    builder.run()