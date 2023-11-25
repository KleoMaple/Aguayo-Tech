from typing import List

from models.Shipment import Shipment

def get_vehicle_shipments(shipments: List[Shipment], vehicle_payload: int):
    """
    Recibe la lista de pedidos y retorna la mejor opcion de pedidos a realizar
    """
    weights = [shipment.get_product().get_weight() for shipment in shipments]
    
    weights.sort()
    
    current_weight = 0
    weights_set = []
    for weight in weights:
        if current_weight + weight > vehicle_payload:
            break
        weights_set.append(weight)
        current_weight += weight
    
    vehicle_shipments = []
    for weight in weights_set:
        for shipment in shipments:
            if shipment.get_product().get_weight() == weight and shipment not in vehicle_shipments:
                vehicle_shipments.append(shipment)
                break
    
    return vehicle_shipments