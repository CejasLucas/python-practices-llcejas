# WebApp/modules/submodules/utils_matplotlib.py
from src.main.utils_matplotlib.exercise1 import run_exercise_1
from src.main.utils_matplotlib.exercise2 import run_exercise_2
from src.main.utils_matplotlib.exercise3 import run_exercise_3
from src.main.utils_matplotlib.exercise4 import run_exercise_4
from src.main.utils_matplotlib.exercise5 import run_exercise_5
from src.main.utils_matplotlib.exercise6 import run_exercise_6

def get_matplotlib_menu_text():
    return (
        "Which Matplotlib exercise would you like to run?\n"
        "1 - Bar chart showing GDP (2019) of Latin American countries.\n"
        "2 - Pie chart with GDP percentage distribution (highlight a specific country).\n"
        "3 - Scatter plot: population vs. surface area for American countries.\n"
        "4 - Grouped bar chart: product outputs over 5 weekdays.\n"
        "5 - Stacked bar chart: coffee, tea, and water consumption over 6 days.\n"
        "6 - Scatter plot: athlete group scores with color coding.\n"
        "0 - Exit."
    )

def get_matplotlib_exercises():
    return {
        1: {"name": "Bar chart of Latin American GDP (2019)", "func": run_exercise_1},
        2: {"name": "GDP percentage pie chart", "func": run_exercise_2},
        3: {"name": "Scatter plot: population vs. surface", "func": run_exercise_3},
        4: {"name": "Grouped bar chart of product outputs", "func": run_exercise_4},
        5: {"name": "Stacked bar chart: beverage consumption", "func": run_exercise_5},
        6: {"name": "Scatter plot: athlete group scores", "func": run_exercise_6},
    }
