import networkx as nx
from src.main.Practices.utils_networkx.style_graph import GraphStyle, build_graph, theme_palette

def get_graph_data():
    return [
        ("A", "B", 4),
        ("A", "E", 8),
        ("E", "F", 6),
        ("F", "D", 8),
        ("B", "C", 5),
        ("F", "G", 9),
        ("C", "G", 8),
        ("G", "H", 11),
        ("F", "H", 11)
    ]

def display_graph_info(path: list[str], cost: float):
    print("\n=== SHORTEST PATH from A to H ===")
    print(" -> ".join(path))
    print(f"Total fuel needed: {cost} units \n")

def highlight_path_subgraph(graph: nx.Graph, path: list[str]) -> nx.Graph:
    edges_in_path = [(path[i], path[i+1]) for i in range(len(path) - 1)]
    path_subgraph = nx.Graph()
    for u, v in edges_in_path:
        weight = graph[u][v]["weight"]
        path_subgraph.add_edge(u, v, weight=weight)
    return path_subgraph

def run_exercise_3():
    graph = build_graph(get_graph_data())
    base_style = GraphStyle()
    base_style.draw_graph_pyvis(graph, "Exercise3 Transportation Map")

    source, target = "A", "H"
    shortest_path = nx.dijkstra_path(graph, source=source, target=target)
    total_cost = nx.dijkstra_path_length(graph, source=source, target=target)

    path_subgraph = highlight_path_subgraph(graph, shortest_path)
    highlight_style = GraphStyle(node_color=theme_palette[2]["node"], edge_color=theme_palette[2]["edge"])
    highlight_style.draw_graph_pyvis(path_subgraph, "Exercise3 Shortest path")

    display_graph_info(shortest_path, total_cost)
