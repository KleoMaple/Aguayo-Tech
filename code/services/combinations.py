from typing import List

from models.Shipment import Shipment

#Método para obtener los pedidos que se pueden realizar con un vehículo
def get_vehicle_shipments(shipments: List[Shipment], vehicle_payload: int):
    """
    Método para obtener los pedidos que se pueden realizar con un vehículo

    ### Recibe como parámetros:
    - shipments: Lista de pedidos
    - vehicle_payload: Carga máxima del vehículo

    ### Retorna:
    - Lista de pedidos que se pueden realizar con un vehículo
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