# WebApp/__utils__/Modules/utils_numpy.py
from Practices.utils_numpy.exercise1 import run_exercise_1
from Practices.utils_numpy.exercise2 import run_exercise_2
from Practices.utils_numpy.exercise3 import run_exercise_3
from Practices.utils_numpy.exercise4 import run_exercise_4

def get_numpy_menu_text():
    return (
        "Which NumPy exercise would you like to run?\n"
        "1 - Matrix operations (subtraction, multiplication, slicing, print last row).\n"
        "2 - Sum and average of matrix elements (loops and NumPy).\n"
        "3 - Create 7x9 matrix with specific columns and average last row.\n"
        "4 - Create 5x5 random matrix, print positions of elements > 0.5.\n"
        "0 - Exit."
    )

def get_numpy_exercises():
    return {
        1: {"name": "Matrix operations and slicing", "func": run_exercise_1},
        2: {"name": "Sum and average of matrix elements", "func": run_exercise_2},
        3: {"name": "7x9 matrix with column patterns", "func": run_exercise_3},
        4: {"name": "5x5 random matrix - positions > 0.5", "func": run_exercise_4},
    }
