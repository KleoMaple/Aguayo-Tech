import networkx as nx

from typing import List
from models.Coordinate import Coordinate

#Función para crear un grafo con las coordenadas de los pedidos
def create_graph(adresses: List[Coordinate]):
    """
    Función para crear un grafo con las coordenadas de los pedidos

    ### Recibe como parámetros:
    - adresses: Lista de coordenadas de los pedidos

    ### Retorna:
    - Grafo con las coordenadas de los pedidos
    """
    g = nx.Graph()
    points = [address.get_point() for address in adresses]

    g.add_nodes_from(points)
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                g.add_edge(points[i], points[j], weight= int(adresses[i].get_distance_to(adresses[j])))
    
    return g
