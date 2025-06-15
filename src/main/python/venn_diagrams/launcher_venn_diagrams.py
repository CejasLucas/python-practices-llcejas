from src.main.python.venn_diagrams.exercise1 import run_exercise_1
from src.main.python.venn_diagrams.exercise2 import run_exercise_2
from src.main.python.venn_diagrams.exercise3 import run_exercise_3
from src.main.python.venn_diagrams.exercise4 import run_exercise_4
from src.main.python.venn_diagrams.exercise5 import run_exercise_5
from src.main.python.venn_diagrams.exercise6 import run_exercise_6
from src.main.python.venn_diagrams.exercise7 import run_exercise_7
from src.main.python.venn_diagrams.exercise8 import run_exercise_8
from src.main.python.venn_diagrams.exercise9 import run_exercise_9
from src.main.python.venn_diagrams.exercise10 import run_exercise_10
from src.main.python.venn_diagrams.exercise11 import run_exercise_11
from colorama import Fore, Style

venn2_colors = {
    '10': '#6BAF92',  # Green
    '01': '#FFF176',  # Yellow
    '11': '#A5D89D'  # Blend of green + yellow (soft lime)
}

venn3_colors = {
    '100': '#6BAF92',  # Green
    '010': '#BDBDBD',  # Gray
    '001': '#FFF176',  # Yellow

    '110': '#94BFA3',  # Green & Gray
    '101': '#CDEB8B',  # Green & Yellow
    '011': '#E3DE9D',  # Gray & Yellow

    '111': '#BFD78A'  # Blend of all three (desaturated soft lime)
}

exercises = {
    1: run_exercise_1,
    2: run_exercise_2,
    3: run_exercise_3,
    4: run_exercise_4,
    5: run_exercise_5,
    6: run_exercise_6,
    7: run_exercise_7,
    8: run_exercise_8,
    9: run_exercise_9,
    10: run_exercise_10,
    11: run_exercise_11
}

def run(number): exercises[number]()

def menu():
    print(Fore.LIGHTWHITE_EX + Style.DIM + "Which exercise would you like to run?")
    print(" 1 - Basic Set Operations in Python")
    print(" 2 - Language Study Venn Diagram")
    print(" 3 - Algebra II and Sports Participation")
    print(" 4 - Python Functions & Venn Symbols")
    print(" 5 - M, N and Universe U Analysis")
    print(" 6 - Tech Ownership among Students")
    print(" 7 - Cardinalities from Venn Diagram")
    print(" 8 - Pet Ownership Survey")
    print(" 9 - Transportation in Buenos Aires")
    print("10 - Family Educational Levels")
    print("11 - Students in Math, Physics & Chemistry")
    print(" 0 - Exit")