from src.main.Modules.dictionaries import get_dictionaries_exercises
from src.main.Modules.dictionaries import get_dict_menu_text
from src.main.Modules.__builder__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_dictionaries_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n================================== COLLECTIONS PRACTICE: DICTIONARIES ==================================")
    builder = ExerciseBuilder(exercises=exercises, menu_text=get_dict_menu_text())
    builder.run()