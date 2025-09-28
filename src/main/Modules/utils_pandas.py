# WebApp/__utils__/Modules/utils_pandas.py
from Practices.utils_pandas.exercise1 import run_exercise_1
from Practices.utils_pandas.exercise2 import run_exercise_2
from Practices.utils_pandas.exercise3 import run_exercise_3
from Practices.utils_pandas.exercise4 import run_exercise_4
from Practices.utils_pandas.exercise5 import run_exercise_5
from Practices.utils_pandas.exercise6 import run_exercise_6
from Practices.utils_pandas.exercise7 import run_exercise_7

def get_pandas_menu_text():
    return (
        "Which Pandas exercise would you like to run?\n"
        "1 - Enter sales by year and apply a 10% discount.\n"
        "2 - Calculate statistics (min, max, mean, std deviation) for student grades.\n"
        "3 - Calculate balance (sales - expenses) for a list of months.\n"
        "4 - Analyze car prices from autos.xlsx (min, max, and average).\n"
        "5 - Analyze comercio_interno.csv (dimensions, plots, sorting, aggregation).\n"
        "6 - Grouping and statistics using users, votes, and movies datasets.\n"
        "7 - Analyze salaries_database.csv (seniority stats, job percentages, salary aggregations).\n"
        "0 - Exit."
    )

def get_pandas_exercises():
    return {
        1: {"name": "Sales discount calculation", "func": run_exercise_1},
        2: {"name": "Student grades statistics", "func": run_exercise_2},
        3: {"name": "Monthly balance calculation", "func": run_exercise_3},
        4: {"name": "Car prices analysis (autos.xlsx)", "func": run_exercise_4},
        5: {"name": "Internal commerce CSV analysis", "func": run_exercise_5},
        6: {"name": "Grouping and stats on datasets", "func": run_exercise_6},
        7: {"name": "Salary database analysis", "func": run_exercise_7}
    }
