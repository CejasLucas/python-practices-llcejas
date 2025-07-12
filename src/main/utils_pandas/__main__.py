from src.main.__utils__.builder import ExerciseBuilder
from src.main.utils_pandas.exercise1 import run_exercise_1
from src.main.utils_pandas.exercise2 import run_exercise_2
from src.main.utils_pandas.exercise3 import run_exercise_3
from src.main.utils_pandas.exercise4 import run_exercise_4
from src.main.utils_pandas.exercise5 import run_exercise_5
from src.main.utils_pandas.exercise6 import run_exercise_6
from src.main.utils_pandas.exercise7 import run_exercise_7
from colorama import Fore, Style

def get_pandas_exercises():
    return {
        1: run_exercise_1,
        2: run_exercise_2,
        3: run_exercise_3,
        4: run_exercise_4,
        5: run_exercise_5,
        6: run_exercise_6,
        7: run_exercise_7
    }

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

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n=========================== PANDAS PRACTICE MENU ===========================")
    builder = ExerciseBuilder(exercises=get_pandas_exercises(), menu_text=get_pandas_menu_text())
    builder.run()