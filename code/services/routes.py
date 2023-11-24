from mocks.shipments import shipments

from services.distances import filter_shipments, get_coordinates
from services.graph import create_graph, draw_graph

from models.Coordinate import Coordinate
from models.Vehicle import Vehicle
from models.Shipment import Shipment

from constants import WAREHOUSE, LIGHT_VEHICLE, HEAVY_VEHICLE

import networkx as nx

from typing import List

visited_points = [] 

def remove_shipments(shipments: List[Shipment], shipments_to_remove: List[Shipment])-> List[Shipment]:
    for shipment in shipments_to_remove:
        shipments.remove(shipment)

    return shipments
   
def get_route(root: Coordinate, g: nx.Graph, vehicle: Vehicle, shipments: List[Shipment]):
    vehicle_shipments = vehicle.get_shipments()
    shipments = remove_shipments(shipments, vehicle_shipments)
    unvisited_points = get_coordinates(vehicle_shipments)

    route = [root]
    unvisited_points.remove(root)
    vehicle_shipments = remove_shipments(vehicle_shipments, [shipment for shipment in vehicle_shipments if shipment.get_client().get_address() == root])

    while unvisited_points:

        next = get_next(g, root)
        if not next:
            break

        if next in unvisited_points:
            unvisited_points.remove(next)
            shipment_to_remove = [shipment for shipment in vehicle_shipments if shipment.get_client().get_address() == next]

            vehicle_shipments = remove_shipments(vehicle_shipments, shipment_to_remove)
            
        route.append(next)

        if len(vehicle_shipments) == 0:
            
            vehicle_shipments = vehicle.fill_vehicle(shipments)
            if not vehicle_shipments:
                break
            
            route.append(WAREHOUSE)

            shipments = remove_shipments(shipments, vehicle_shipments)
            unvisited_points = get_coordinates(vehicle_shipments)
            
            g = create_graph(unvisited_points)
            next = max(unvisited_points)
        
        root = next
        
    return route

def get_next(g: nx.Graph, root: Coordinate) -> Coordinate:
    
    if not root: 
        return None
    root_edges = list(g.edges(root.get_point()))
    
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
        
def print_route(route: List[Coordinate], vehicle: Vehicle):

    print(f"|{'-'*10}|{'-'*20}|")
    print(f"|{'RUTA': <10}|{'DIRECCIÓN': <20}|")
    print(f"|{'-'*10}|{'-'*20}|")
    for point in route:
        print(f"|{vehicle.get_id(): <10}|{str(point.get_point()): <20}|")
    print(f"|{'-'*10}|{'-'*20}|")
    
def main():

    shipments_beyond, shipments_within = filter_shipments(shipments)
    
    LIGHT_VEHICLE.fill_vehicle(shipments_beyond.copy())
    HEAVY_VEHICLE.fill_vehicle(shipments_within.copy())
    
    points_beyond = get_coordinates(LIGHT_VEHICLE.get_shipments())
    points_within = get_coordinates(HEAVY_VEHICLE.get_shipments())
    
    g_beyond = create_graph(points_beyond)
    g_within = create_graph(points_within)

    root_beyond = max(points_beyond)
    visited_points.append(root_beyond)

    visited_points.clear()
    root_within = max(points_within)
    visited_points.append(root_within)
    
    route_beyond = get_route(
        root_beyond, 
        g_beyond, 
        LIGHT_VEHICLE,
        shipments_beyond.copy()
    )

    route_within = get_route(
        root_within, 
        g_within,  
        HEAVY_VEHICLE,
        shipments_within.copy()
    )
    
    print('\n\n')
    print_route(route_beyond, LIGHT_VEHICLE)
    print(f"PEDIDOS TOTALES: {len(shipments_beyond)}, PEDIDOS ENTREGADOS: {len(route_beyond)}")
    print('\n\n')
    print_route(route_within, HEAVY_VEHICLE)
    print(f"PEDIDOS TOTALES: {len(shipments_within)}, PEDIDOS ENTREGADOS: {len(route_within)}")


if __name__ == '__main__':
    main()
    