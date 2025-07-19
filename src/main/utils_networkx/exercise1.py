import networkx as nx
import matplotlib.pyplot as plt

def data():
    return [
        ("Z", "E", 3), ("Z", "F", 2), ("Z", "C", 1),
        ("F", "E", 1), ("F", "C", 1),
        ("E", "D", 2), ("C", "B", 5),
        ("D", "G", 1), ("B", "G", 1),
        ("B", "A", 4), ("G", "A", 2), ("D", "A", 5)
    ]

def start_graph():
    graph = nx.Graph()
    graph.add_weighted_edges_from(data())
    return graph

def draw_graph(graph):
    pos = nx.shell_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_color="red", node_size=1000, alpha=0.9)
    nx.draw_networkx_labels(graph, pos, font_size=10, font_family="sans-serif")
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edges(graph, pos, edge_color="black", width=3)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.gcf().canvas.manager.set_window_title("Exercise 1")
    plt.suptitle("Graph: Dijkstra's path algorithms", fontsize=12, fontweight='bold')
    plt.axis("off")
    plt.show()

def print_info(graph):
    print("All NODES:")
    print(graph.nodes())
    print("Number of NODES:", graph.number_of_nodes())
    print()

    print("All EDGES:")
    print(graph.edges())
    print("Number of EDGES:", graph.number_of_edges())
    print()

    shortest_path = nx.dijkstra_path(graph, "Z", "A")
    path_length = nx.dijkstra_path_length(graph, "Z", "A")

    print("Shortest path from Z to A:", shortest_path)
    print("Shortest path length:", path_length)
    print()

    adj_matrix = nx.adjacency_matrix(graph)
    print("Adjacency Matrix:")
    print(adj_matrix.todense())
    print()

    inc_matrix = nx.incidence_matrix(graph)
    print("Incidence Matrix:")
    print(inc_matrix.todense())
    print()

def run_exercise_1():
    graph = start_graph()
    draw_graph(graph)
    print_info(graph)
