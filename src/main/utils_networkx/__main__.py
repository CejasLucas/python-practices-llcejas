from src.main.__utils__.builder import ExerciseBuilder
from src.main.utils_networkx.exercise1 import run_exercise_1
from src.main.utils_networkx.exercise2 import run_exercise_2
from src.main.utils_networkx.exercise3 import run_exercise_3
from src.main.utils_networkx.exercise4 import run_exercise_4
from src.main.utils_networkx.exercise5 import run_exercise_5
from src.main.utils_networkx.exercise6 import run_exercise_6
from colorama import Fore, Style

def get_networkx_exercises():
    return {
        1: run_exercise_1,
        2: run_exercise_2,
        3: run_exercise_3,
        4: run_exercise_4,
        5: run_exercise_5,
        6: run_exercise_6
    }

def get_networkx_menu_text():
    return (
        "NetworkX and Graph Theory Practice\n"
        "1 - Use Dijkstra's algorithm to find the shortest path between vertices Z and A in a weighted graph.\n"
        "2 - Find the cheapest telephone network design to connect all points in an urban area. Also compute: radius, diameter, eccentricity, center, periphery, and density.\n"
        "3 - Given a weighted graph of 8 cities (A to H) with fuel consumption as weights, calculate the minimum fuel needed to travel from A to H.\n"
        "4 - For a graph representing cities and distances.\n"
        "5 - Two friends want to visit Prague. Draw the graph with landmarks and distances, and analyze travel routes.\n"
        "6 - Analyze computer connections among 12 employees.\n"
        "7 - Generate the adjacency and incidence matrices for all provided graph scenarios.\n"
        "0 - Exit."
    )

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n=========================== PRÁCTICA NETWORKX Y GRAFOS ===========================")
    builder = ExerciseBuilder(exercises=get_networkx_exercises(), menu_text=get_networkx_menu_text())
    builder.run()