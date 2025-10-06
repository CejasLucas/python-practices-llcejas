import networkx as nx
from src.main.Practices.utils_networkx.style_graph import GraphStyle, build_graph, theme_palette

pairs = [
    ("Escobar", "Fernandez"),
    ("Gonzalez", "Herrera"),
    ("Alvarez", "Benitez"),
    ("Cejas", "Dominguez"),
    ("Ibarra", "Juarez")
]

def get_initial_graph_data():
    return [
        ("Dominguez", "Fernandez", 11),
        ("Dominguez", "Gonzalez", 13),
        ("Escobar", "Fernandez", 12),
        ("Fernandez", "Herrera", 14),
        ("Fernandez", "Ibarra", 12),
        ("Gonzalez", "Juarez", 10),
        ("Benitez", "Dominguez", 7),
        ("Alvarez", "Benitez", 2),
        ("Herrera", "Juarez", 8),
        ("Ibarra", "Juarez", 3),
        ("Escobar", "Cejas", 2),
        ("Alvarez", "Cejas", 6),
        ("Juarez", "Lopez", 9),
    ]

def check_pairing(graph: nx.Graph):
    print("Checking if all required pairs are directly connected:")
    all_connected = True
    for u, v in pairs:
        if not graph.has_edge(u, v) and not graph.has_edge(v, u):
            print(f"Pair {u} – {v} is NOT connected")
            all_connected = False
        else:
            print(f"Pair {u} – {v} is connected")
    return all_connected


def display_graph_info(graph: nx.Graph):
    print("\n=== Part A: Check Pair Connections ===")
    all_connected = check_pairing(graph)
    if all_connected:
        print("\nAll pairs can work together (direct connection exists).")
    else:
        print("\nNot all pairs are directly connected — pairing as requested is NOT fully possible.")

    print("\n=== Part B: Shortest Path from Alvarez to Juarez ===")
    source = "Alvarez"
    target = "Juarez"
    try:
        path = nx.dijkstra_path(graph, source, target)
        total = nx.dijkstra_path_length(graph, source, target)
        print(" → ".join(path))
        print(f"Total cable length: {total} meters \n")
    except nx.NetworkXNoPath:
        print(f"No path exists between {source} and {target}. \n")


def run_exercise_6():
    graph = build_graph(get_initial_graph_data())
    style = GraphStyle(node_color=theme_palette[1]["node"], edge_color=theme_palette[1]["edge"])
    style.draw_graph_pyvis(graph, "Exercise6 Office Network")

    display_graph_info(graph)