import os
import webbrowser
import networkx as nx
from pathlib import Path
from pyvis.network import Network

OUTPUT_DIR = "outputs"

theme_palette = {
    1: {"node": "#345E44", "edge": "#63A86E"},
    2: {"node": "#19404C", "edge": "#63757D"},
    3: {"node": "#7B5C3F", "edge": "#C3A481"},
    4: {"font": "#0A0A0A", "label": "#404040"}
}

def build_graph(data):
    graph = nx.Graph()
    graph.add_weighted_edges_from(data)
    return graph


class GraphStyle:
    edge_font_size = 10
    node_font_size = 25
    node_size = 30

    def __init__(
            self,
            node_color=theme_palette[1]["node"],
            node_font_color=theme_palette[4]["label"],
            edge_color=theme_palette[1]["edge"],
            edge_label_color=theme_palette[4]["font"]
    ):
        self.node_color = node_color
        self.node_font_color = node_font_color
        self.edge_color = edge_color
        self.edge_label_color = edge_label_color

    def draw_graph_pyvis(self, graph, title):
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        net = Network(height="750px", width="100%", directed=False, notebook=False)

        for node in graph.nodes():
            net.add_node(
                node,
                label=node,
                color=self.node_color,
                font={'size': self.node_font_size, 'color': self.node_font_color, 'bold': True},
                size=self.node_size
            )

        for u, v, data_edge in graph.edges(data=True):
            weight = data_edge.get('weight', 1)
            net.add_edge(
                u, v,
                value=weight,
                width=weight,
                label=str(weight),
                title=f"Peso: {weight}",
                color=self.edge_color,
                font={'size': self.edge_font_size, 'color': self.edge_label_color}
            )

        net.show_buttons(filter_=['physics'])

        net.barnes_hut(
            spring_length=50,
            spring_strength=0.005,
            gravity=-2000,
            central_gravity=0.3,
            damping=0.09,
            overlap=0.1
        )

        file_name = f"{title.replace(' ', '_').lower()}.html"
        file_path = os.path.join(OUTPUT_DIR, file_name)
        net.save_graph(file_path)

        abs_path = Path(file_path).absolute().as_uri()  # <-- STOP
        print(f"HTML generado en: {abs_path}")
        webbrowser.open(abs_path)