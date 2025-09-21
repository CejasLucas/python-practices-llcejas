# WebApp/modules/submodules/utils_networkx.py
from src.main.utils_networkx.exercise1 import run_exercise_1
from src.main.utils_networkx.exercise2 import run_exercise_2
from src.main.utils_networkx.exercise3 import run_exercise_3
from src.main.utils_networkx.exercise4 import run_exercise_4
from src.main.utils_networkx.exercise5 import run_exercise_5
from src.main.utils_networkx.exercise6 import run_exercise_6

def get_networkx_menu_text():
    return (
        "NetworkX and Graph Theory Practice\n"
        "1 - Use Dijkstra's algorithm to find the shortest path between vertices Z and A in a weighted graph.\n"
        "2 - Find the cheapest telephone network design. Also compute: radius, diameter, eccentricity, center, periphery, and density.\n"
        "3 - Minimum fuel needed from city A to H in a weighted graph.\n"
        "4 - Analyze distances between cities in a graph.\n"
        "5 - Friends visiting Prague: draw landmarks and analyze routes.\n"
        "6 - Analyze computer connections among 12 employees.\n"
        "0 - Exit."
    )

def get_networkx_exercises():
    return {
        1: {"name": "Dijkstra shortest path (Z to A)", "func": run_exercise_1},
        2: {"name": "Minimal telephone network & analysis", "func": run_exercise_2},
        3: {"name": "Fuel optimization between cities (A to H)", "func": run_exercise_3},
        4: {"name": "Distance analysis between cities", "func": run_exercise_4},
        5: {"name": "Trip to Prague: routes & landmarks", "func": run_exercise_5},
        6: {"name": "Employee computer network analysis", "func": run_exercise_6},
    }
