from services.shipments import filter_shipments, get_coordinates, get_shipments_by_coordinates, get_shipments
from services.graph import create_graph

from models.Coordinate import Coordinate
from models.Vehicle import Vehicle
from models.Shipment import Shipment
from models.Route import Route

from constants import WAREHOUSE, LIGHT_VEHICLE, HEAVY_VEHICLE

import networkx as nx

from typing import List

visited_points = [] 

#Función para eliminar los pedidos que ya fueron asignados a un vehículo
def remove_shipments(shipments: List[Shipment], shipments_to_remove: List[Shipment])-> List[Shipment]:
    """
    Función para eliminar los pedidos que ya fueron asignados a un vehículo

    ### Recibe como parámetros:
    - shipments: Lista de pedidos
    - shipments_to_remove: Lista de pedidos a eliminar

    ### Retorna:
    - Lista de pedidos sin los pedidos que ya fueron asignados a un vehículo
    """
    for shipment in shipments_to_remove:
        shipments.remove(shipment)

    return shipments

#Función para obtener la ruta más corta entre un punto de partida y los demás puntos
def get_route(root: Coordinate, g: nx.Graph, vehicle: Vehicle, shipments: List[Shipment]) -> List[Coordinate]:
    """
    Algoritmo para calcular la ruta más corta entre un punto de partida y los demás puntos

    ### Recibe como parámetros:
    - root: Punto de partida
    - g: Grafo con las coordenadas de los puntos
    - vehicle: Vehículo que realizará la ruta
    - shipments: Lista de pedidos

    ### Retorna:
    - Lista de coordenadas con la ruta más corta
    """
    vehicle_shipments = vehicle.get_shipments()
    unvisited_points = get_coordinates(shipments)
    shipments = remove_shipments(shipments, vehicle_shipments)

    route = [root] #Se agrega el punto de partida a la ruta

    unvisited_points.remove(root) #Se elimina el punto de partida de los puntos no visitados

    #Se eliminan los pedidos que se encuentran en el punto de partida
    vehicle_shipments = remove_shipments(vehicle_shipments, [shipment for shipment in vehicle_shipments if shipment.get_client().get_address() == root])

    while unvisited_points:
        #Se obtiene la siguiente coordenada más cercana a la raíz
        next = get_next(g, root)

        if not next and unvisited_points:
            
            next = max(get_coordinates(vehicle_shipments))
            g = create_graph(get_coordinates(vehicle_shipments))
            
        elif not next: 
            break

        if next in unvisited_points:
            #Se elimina el siguiente nodo de los nodos no visitados
            unvisited_points.remove(next)

            #Se recupera el pedido asociado a next
            shipment_to_remove = [shipment for shipment in vehicle_shipments if shipment.get_client().get_address() == next]

            #Se elimina el pedido de los pedidos del vehículo
            vehicle_shipments = remove_shipments(vehicle_shipments, shipment_to_remove)

            #Se agrega el siguiente nodo a la ruta
            route.append(next)
        
        #Si no quedan pedidos por entregar se llena el vehículo
        if not vehicle_shipments:
            #Se llena el vehículo con los pedidos que quedan por entregar y se asignan a vehicle_shipments
            vehicle_shipments = vehicle.fill_vehicle(shipments)

            if not vehicle_shipments:
                break
            
            #Se agrega el punto de partida a la ruta
            route.append(WAREHOUSE)
            shipments = remove_shipments(shipments, vehicle_shipments)
            g = create_graph(get_coordinates(vehicle_shipments))
            next = max(get_coordinates(vehicle_shipments))
        
        root = next

    return route

#Función para obtener el siguiente punto más cercano a la raíz
def get_next(g: nx.Graph, root: Coordinate) -> Coordinate:
    """
    Función para obtener el siguiente punto más cercano a la raíz

    ### Recibe como parámetros:
    - g: Grafo con las coordenadas de los puntos
    - root: Punto de partida

    ### Retorna:
    - Siguiente punto más cercano a la raíz
    """
    if not root: 
        return None
    
    root_edges = list(g.edges(root.get_point())) #Se obtienen las aristas de la raíz
    
    distances_to_root = []
    points = []

    for edge in root_edges:

        point = Coordinate(edge[1][0], edge[1][1])

        if point in visited_points:
        
            continue

        distance_to_root = root.get_distance_to(point)
        points.append(point)

        distances_to_root.append(distance_to_root)
    
    if distances_to_root:
        next = points[distances_to_root.index(min(distances_to_root))]
        visited_points.append(next)
    else:
        next = None

    return next

#Función para obtener las rutas de los vehículos   
def get_routes():
    """
    Función para obtener las rutas de los vehículos
    
    ### Retorna:
    - Ruta del vehículo liviano
    - Ruta del vehículo pesado
    """
    shipments_beyond, shipments_within = filter_shipments(get_shipments())

    if not shipments_beyond:
        route_within = calculate_route(shipments_within, HEAVY_VEHICLE)
        route_beyond = Route([])
    elif not shipments_within:
        route_beyond = calculate_route(shipments_beyond, LIGHT_VEHICLE)
        route_within = Route([])
    else:
        route_beyond = calculate_route(shipments_beyond, LIGHT_VEHICLE)
        visited_points.clear()
        route_within = calculate_route(shipments_within, HEAVY_VEHICLE)

    return route_beyond, route_within


#Función para calcular la ruta de un vehículo    
def calculate_route(shipments: List[Shipment], vehicle: Vehicle) -> Route:
    """
    Función para calcular la ruta de un vehículo 
    
    ### Recibe como parámetros:
    - shipments: Lista de pedidos
    - vehicle: Vehículo que realizará la ruta

    ### Retorna:
    - Ruta del vehículo
    """
    vehicle.fill_vehicle(shipments.copy())
    points = get_coordinates(vehicle.get_shipments())
    graph = create_graph(points)
    
    root = max(points)
    visited_points.append(root)

    route_coordinates = get_route(
        root, 
        graph, 
        vehicle,
        shipments.copy()
    )

    route = Route(get_shipments_by_coordinates(route_coordinates, shipments))
    return route


if __name__ == '__main__':
    get_routes()