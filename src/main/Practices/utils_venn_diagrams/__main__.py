from src.main.Modules.utils_venn_diagrams import get_venn_diagrams_exercises, get_venn_diagrams_menu_text
from src.main.Modules.__builder__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_venn_diagrams_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n================== VENN DIAGRAMS PRACTICE ==================" + Style.RESET_ALL)

    builder = ExerciseBuilder(exercises=exercises, menu_text=get_venn_diagrams_menu_text())
    builder.run()