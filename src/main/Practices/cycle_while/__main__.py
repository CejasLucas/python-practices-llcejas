from src.main.Practices.cycle_while.__menu__ import get_cycle_while_exercises
from src.main.Practices.__loader__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_cycle_while_exercises().items()}
    submenu = {k: v["name"] for k, v in get_cycle_while_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n========================= WHILE CYCLE PRACTICE =========================" + Style.RESET_ALL)

    builder = ExerciseBuilder(exercises=exercises, menu=submenu)
    builder.run()