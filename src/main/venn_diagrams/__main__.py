from src.main.__utils__.builder import ExerciseBuilder
from src.main.venn_diagrams.exercise1 import run_exercise_1
from src.main.venn_diagrams.exercise2 import run_exercise_2
from src.main.venn_diagrams.exercise3 import run_exercise_3
from src.main.venn_diagrams.exercise4 import run_exercise_4
from src.main.venn_diagrams.exercise5 import run_exercise_5
from src.main.venn_diagrams.exercise6 import run_exercise_6
from src.main.venn_diagrams.exercise7 import run_exercise_7
from src.main.venn_diagrams.exercise8 import run_exercise_8
from src.main.venn_diagrams.exercise9 import run_exercise_9
from src.main.venn_diagrams.exercise10 import run_exercise_10
from colorama import Fore, Style

def get_venn_diagrams_exercises():
    return {
        1: run_exercise_1,
        2: run_exercise_2,
        3: run_exercise_3,
        4: run_exercise_4,
        5: run_exercise_5,
        6: run_exercise_6,
        7: run_exercise_7,
        8: run_exercise_8,
        9: run_exercise_9,
        10: run_exercise_10
    }

def get_venn_diagrams_menu_text():
    return (
            "Which exercise would you like to run?\n"
            " 1 - Basic Set Operations in Python.\n"
            " 2 - Language Study Venn Diagram.\n"
            " 3 - Algebra II and Sports Participation.\n"
            " 4 - M, N and Universe U Analysis.\n"
            " 5 - Tech Ownership among Students.\n"
            " 6 - Cardinalities from Venn Diagram.\n"
            " 7 - Pet Ownership Survey.\n"
            " 8 - Transportation in Buenos Aires.\n"
            " 9 - Family Educational Levels.\n"
            " 10 - Students in Math, Physics & Chemistry.\n"
            " 0 - Exit."
    )

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n================== VENN DIAGRAMS PRACTICE ==================" + Style.RESET_ALL)
    builder = ExerciseBuilder(exercises=get_venn_diagrams_exercises(), menu_text=get_venn_diagrams_menu_text())
    builder.run()