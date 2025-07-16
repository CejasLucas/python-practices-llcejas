from src.main.__utils__.builder import ExerciseBuilder
from src.main.utils_matplotlib.exercise1 import run_exercise_1
from src.main.utils_matplotlib.exercise2 import run_exercise_2
from src.main.utils_matplotlib.exercise3 import run_exercise_3
from src.main.utils_matplotlib.exercise4 import run_exercise_4
from src.main.utils_matplotlib.exercise5 import run_exercise_5
from src.main.utils_matplotlib.exercise6 import run_exercise_6
from colorama import Fore, Style

def get_matplotlib_exercises():
    return {
        1: run_exercise_1,
        2: run_exercise_2,
        3: run_exercise_3,
        4: run_exercise_4,
        5: run_exercise_5,
        6: run_exercise_6
    }

def get_matplotlib_menu_text():
    return (
        "Which Pandas exercise would you like to run?\n"
        "1 - Create a bar chart showing the GDP (2019) of Latin American countries.\n"
        "2 - Generate a pie chart with the GDP percentage distribution and highlight a specific country.\n"
        "3 - Plot population vs. surface area for American countries.\n"
        "4 - Create a grouped bar chart comparing two product outputs over 5 weekdays.\n"
        "5 - Generate a stacked bar chart of coffee, tea, and water consumption over 6 days for several people.\n"
        "6 - Plot a scatter plot with two athlete group scores across a defined range, using color coding.\n"
        "0 - Exit."
    )

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n=========================== MATPLOTLIB PRACTICE MENU ===========================")
    builder = ExerciseBuilder(exercises=get_matplotlib_exercises(), menu_text=get_matplotlib_menu_text())
    builder.run()