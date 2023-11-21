import networkx as nx
import matplotlib.pyplot as plt

from typing import List
from models.Coordinate import Coordinate


def create_graph(adresses: List[Coordinate]):
    g = nx.Graph()
    points = [address.get_point() for address in adresses]

    g.add_nodes_from(points)
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                g.add_edge(points[i], points[j], weight= int(adresses[i].get_distance_to(adresses[j])))
    
    return g


def draw_graph(g: nx.Graph):
    pos = nx.spring_layout(g)
    nx.draw_networkx_nodes(g, pos, node_size=700)
    nx.draw_networkx_edges(g, pos, width=6)
    nx.draw_networkx_labels(g, pos, font_size=20, font_family='sans-serif')
    edge_labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
    plt.axis('off')
    plt.show()