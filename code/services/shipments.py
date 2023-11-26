from typing import List
from models.Shipment import Shipment
from models.Coordinate import Coordinate

from constants import VEHICLE_LIMIT, WAREHOUSE, WAREHOUSE_SHIPMENT, ORDERS_PATH

import json

def get_shipments():
    """
        Retorna una lista de pedidos desde el archivo JSON
    """
    shipments = []
    try:
        with open(ORDERS_PATH, 'r', encoding="UTF-8") as file:
            data = json.load(file)
            orders = data['orders']

            for order in orders:
                shipment = Shipment()
                shipment.deserialize(order)
                shipments.append(shipment)

            file.close()
    except FileNotFoundError:
        return []   
    
    return shipments

#Método para filtrar los pedidos según su distancia respecto al almacén
def filter_shipments(shipments: List[Shipment]):
    """
        Recibe una lista de pedidos y los filtra según su distancia.

        Retorna dos arreglos con los pedidos divididos en dos grupos:
        - Los que están dentro del límite
        - Los que están fuera del límite
    """
    shipments_beyond = []
    shipments_within = []

    for shipment in shipments:
        if shipment.get_client().get_address().get_distance() > VEHICLE_LIMIT:
            shipments_beyond.append(shipment)
        else:
            shipments_within.append(shipment)

    return shipments_beyond, shipments_within

#Método para obtener las coordenadas de los pedidos
def get_coordinates(shipments: List[Shipment]) -> List[Coordinate]:
    """
        Recibe una lista de pedidos y retorna una lista con las coordenadas de cada pedido
    """
    coordinates = [ shipment.get_client().get_address() for shipment in shipments ]

    return coordinates

#Método para obtener los pedidos en base a las coordenadas de la ruta
def get_shipments_by_coordinates(route_addresses :List[Coordinate], total_shipments: List[Shipment]) -> List[Shipment]:
    """
        Retorna una lista de pedidos según las coordenadas de la ruta
    """
    shipments_route = []
    for point in route_addresses:
        for shipment in total_shipments:
            if point == shipment.get_client().get_address():
                shipments_route.append(shipment)
                break
            elif point == WAREHOUSE:
                shipments_route.append(WAREHOUSE_SHIPMENT)
                break

    return shipments_route