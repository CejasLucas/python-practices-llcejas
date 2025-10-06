from src.main.Practices.dictionaries.__menu__ import get_dictionaries_exercises
from src.main.Practices.__loader__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_dictionaries_exercises().items()}
    submenu = {k: v["name"] for k, v in get_dictionaries_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n================================== COLLECTIONS PRACTICE: DICTIONARIES ==================================")
    builder = ExerciseBuilder(exercises=exercises, menu=submenu)
    builder.run()