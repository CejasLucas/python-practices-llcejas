import networkx as nx
from src.main.utils_networkx.style_graph import GraphStyle, build_graph, theme_palette

def get_graph_data():
    return [
        ("a", "b", 6), ("a", "c", 9), ("a", "d", 3), ("b", "c", 10),
        ("b", "e", 12), ("c", "d", 4), ("c", "e", 3), ("c", "f", 2),
        ("d", "g", 10), ("d", "f", 15), ("e", "f", 8), ("e", "h", 4),
        ("f", "g", 9), ("f", "i", 10), ("g", "j", 13), ("h", "i", 7),
        ("h", "k", 20), ("i", "j", 15), ("i", "l", 11), ("j", "m", 9),
        ("k", "l", 13), ("k", "n", 6), ("l", "m", 5), ("l", "n", 12), ("m", "n", 5)
    ]


def display_graph_info(mst):
    print("\n=== GRAPH PROPERTIES (on MST) ===")
    print(f"Radius: {nx.radius(mst)}")
    print(f"Center: {nx.center(mst)}")
    print(f"Density: {nx.density(mst):.4f}")
    print(f"Diameter: {nx.diameter(mst)}")
    print(f"Periphery: {nx.periphery(mst)}")
    print("Eccentricity per node:", nx.eccentricity(mst))
    print("\n=== MINIMUM SPANNING TREE ===")
    for u, v, w in mst.edges(data='weight'):
        print(f"{u} - {v} (Cost: {w} thousand $)")
    print("\n")


def run_exercise_2():
    info = [(u.upper(), v.upper(), w) for u, v, w in get_graph_data()]

    graph = build_graph(info)
    style_graph = GraphStyle()
    style_graph.draw_graph_pyvis(graph, "Exercise2 Original Telephone Graph")

    mst = nx.minimum_spanning_tree(graph)
    style_graph_mst = GraphStyle(node_color=theme_palette[3]["node"], edge_color=theme_palette[3]["edge"])
    style_graph_mst.draw_graph_pyvis(mst, "Exercise2 Minimum Spanning Tree Graph")

    display_graph_info(mst)