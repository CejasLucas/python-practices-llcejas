import os
import webbrowser
import networkx as nx
from pyvis.network import Network

OUTPUT_DIR = "/home/usuario/Documentos/GitHub/python-practices-llcejas/outputs"

def data():
    return [
        ("a", "b", 6), ("a", "c", 9), ("a", "d", 3), ("b", "c", 10),
        ("b", "e", 12), ("c", "d", 4), ("c", "e", 3), ("c", "f", 2),
        ("d", "g", 10), ("d", "f", 15), ("e", "f", 8), ("e", "h", 4),
        ("f", "g", 9), ("f", "i", 10), ("g", "j", 13), ("h", "i", 7),
        ("h", "k", 20), ("i", "j", 15), ("i", "l", 11), ("j", "m", 9),
        ("k", "l", 13), ("k", "n", 6), ("l", "m", 5), ("l", "n", 12), ("m", "n", 5)
    ]

def start_graph():
    graph = nx.Graph()
    graph.add_weighted_edges_from(data())
    return graph


def draw_graph_pyvis(graph, title="Interactive Graph"):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    net = Network(height="750px", width="100%", directed=False, notebook=False)
    net.from_nx(graph)

    for node in net.nodes:
        node['color'] = "darkred"
        node['font'] = {'size': 20, 'color': 'black'}

    for edge in net.edges:
        from_node = edge['from']
        to_node = edge['to']
        weight = graph.get_edge_data(from_node, to_node).get('weight', 1)

        edge['value'] = weight
        edge['width'] = weight
        edge['title'] = f"Peso: {weight}"
        edge['label'] = str(weight)
        edge['font'] = {'color': 'darkblue', 'size': 16}
        edge['color'] = "gray"

    net.show_buttons(filter_=['physics'])

    file_name = f"{title.replace(' ', '_').lower()}.html"
    file_path = os.path.join(OUTPUT_DIR, file_name)
    net.save_graph(file_path)

    print(f"HTML generado en: {file_path}")
    webbrowser.open(f"file://{file_path}")


def print_info(mst):
    radius = nx.radius(mst)
    center = nx.center(mst)
    density = nx.density(mst)
    diameter = nx.diameter(mst)
    periphery = nx.periphery(mst)
    eccentricities = nx.eccentricity(mst)

    print("=== MINIMUM SPANNING TREE ===")
    print("Edges in the MST (cheapest design):")
    for u, v, w in mst.edges(data='weight'):
        print(f"{u} - {v} (Cost: {w} thousand $)")

    print("\n=== GRAPH PROPERTIES (on MST) ===")
    print("Eccentricity per node:", eccentricities)
    print(f"Radius: {radius}")
    print(f"Center: {center}")
    print(f"Density: {density:.4f}")
    print(f"Diameter: {diameter}")
    print(f"Periphery: {periphery}")

def run_exercise_2():
    graph = start_graph()
    draw_graph_pyvis(graph, "Original Graph")

    mst = nx.minimum_spanning_tree(graph)
    draw_graph_pyvis(mst, "Minimum Spanning Tree")

    print_info(mst)