from typing import List
from models.Shipment import Shipment

from constants import NORTH_EAST, NORTH_WEST, SOUTH_EAST, SOUTH_WEST
from constants import VEHICLE_LIMIT

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


def get_addresses(shipments: List[Shipment]) -> List[int]:
    """
        Recibe una lista de pedidos y retorna una lista con las distancias de cada pedido
    """
    distances = [ shipment.get_client().get_address() for shipment in shipments ]

    return distances