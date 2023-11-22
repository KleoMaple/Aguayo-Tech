from mocks.shipments import shipments

from services.distances import filter_shipments, get_addresses, get_coordinates
from services.graph import create_graph, draw_graph

from models.Coordinate import Coordinate
from models.Vehicle import Vehicle

from constants import WAREHOUSE, LIGHT_VEHICLE, HEAVY_VEHICLE

import networkx as nx

from typing import List

visited_points = []

def get_route(root: Coordinate, g: nx.Graph, unvisited_points: List[Coordinate], vehicle_limit: int):
    VEHICLE_LIMIT = vehicle_limit
    
    route = [root]
    unvisited_points.remove(root)
    vehicle_limit -= 1

    while unvisited_points:
        if vehicle_limit == 0:
            route.append(WAREHOUSE)
            vehicle_limit = VEHICLE_LIMIT

        next = get_next(g, root)

        if not next:
            break

        route.append(next)

        if next in unvisited_points:
            unvisited_points.remove(next)

        root = next
        vehicle_limit -= 1

    return route
    


def get_next(g: nx.Graph, root: Coordinate) -> Coordinate:

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

    distances_beyond = get_addresses(shipments_beyond)
    distances_within = get_addresses(shipments_within)

    points_beyond = get_coordinates(shipments_beyond)
    points_within = get_coordinates(shipments_within)

    g_beyond = create_graph(distances_beyond)
    g_within = create_graph(distances_within)

    root_beyond = max(distances_beyond)
    visited_points.append(root_beyond)

    visited_points.clear()
    root_within = max(distances_within)
    visited_points.append(root_within)

    draw_graph(g_beyond)
    route_beyond = get_route(root_beyond, g_beyond, points_beyond, LIGHT_VEHICLE.get_payload())

    draw_graph(g_within)
    route_within = get_route(root_within, g_within, points_within, HEAVY_VEHICLE.get_payload())
    
    print('\n\n')
    print_route(route_beyond, LIGHT_VEHICLE)
    print('\n\n')
    print_route(route_within, HEAVY_VEHICLE)


if __name__ == '__main__':
    main()
    