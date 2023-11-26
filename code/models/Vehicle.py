from typing import List
from models.Shipment import Shipment
from services.subsets import subsets, get_below_weight_sets

import json

class Vehicle:
    """
    ## Clase Vehiculo\n
    clase para definir los vehículos que usarán las rutas

    ### Atributos\n
    - id -> string \n
    - payload -> int\n
    - shipments -> list[Shipment]

    ### Métodos\n
    - get_id()\n
    - get_payload()\n
    - set_id( id: string )\n
    - set_payload( payload: int )\n
    """

    #Constructor
    def __init__(self, id: str = None, payload: int = None, shipments: List[Shipment] = None) -> None:
        """
        Constructor de la clase vehículo.

        Puede recibir dos parámetros o en caso de 
        no recibirlos inicializa los atributos en None
        """
        self._id = id
        self._payload = payload
        self._current_payload = 0
        self._shipments = shipments

    #Método get del ID
    def get_id(self) -> str:
        """
        Retorna el ID del vehículo
        """
        return self._id
    
    #Método get del límite de carga
    def get_payload(self) -> int:
        """
        Retorna el límite de carga del vehículo
        """
        return self._payload
    
    #Método get de los pedidos
    def get_shipments(self) -> List[Shipment]:
        """
        Retorna los pedidos del vehículo
        """
        return self._shipments
    
    #Método get de la carga actual
    def get_current_payload(self) -> int:
        """
        Retorna la carga actual del vehículo
        """
        return self._current_payload
    
    #Método set del id del vehículo
    def set_id(self, id: str) -> None:
        """
        Establece el ID del vehículo
        """
        self._id = id

    #Método set del límite de carga
    def set_payload(self, payload: int) -> None:
        """
        Establece el límite de carga del vehículo
        """
        self._payload = payload
    
    #Método set de la carga actual
    def set_current_payload(self, current_payload: int) -> None:
        """
        Establece la carga actual del vehículo
        """
        self._current_payload = current_payload

    #Método set de los pedidos
    def set_shipments(self, shipments: List[Shipment]) -> None:
        """
        Establece los pedidos del vehículo
        """
        if len(shipments) > self._payload:
            raise Exception("La cantidad de pedidos supera el límite de carga")
        
        self._shipments = shipments

    #Método para agregar un pedido
    def fill_vehicle(self, shipments: List[Shipment]) -> None:
        """
        Llena el vehículo con la mejor combinacion de pedidos

        retorna las coordenadas de los pedidos
        """
        weights = [ shipment.get_product().get_weight() for shipment in shipments ]
        weights_subsets = subsets(weights)
        below_weight_sets = get_below_weight_sets(weights_subsets, self._payload)

        max_len_set = max(below_weight_sets, key=len)
        shipments = [ shipment for shipment in shipments if shipment.get_product().get_weight() in max_len_set ]
        
        self.set_shipments(shipments)
        self.set_current_payload(sum(max_len_set))
    
        
        return shipments
    
    #Método igual que
    def __eq__(self, other: object) -> bool:
        """
        Evalúa si el límite de carga es igual
        """
        if isinstance(other, Vehicle):
            return self._payload == other._payload
        return False
    
    #Método diferente que
    def __ne__(self, other: object) -> bool:
        """
        Evalúa si los limites de carga son diferentes
        """
        return not self.__eq__(other)

    #Método menor que
    def __lt__(self, other: object) -> bool:
        """
        Evalúa si el límite de carga es menor al del otro vehículo
        """
        if isinstance(other, Vehicle):
            return self._payload < other._payload
        
        return NotImplemented

    #Método menor o igual que
    def __le__(self, other: object) -> bool:
        """
        Evalúa si el límite de carga es menor o igual al del otro vehículo
        """
        return self.__lt__(other) or self.__eq__(other)
    
    #Método mayor que
    def __gt__(self, other: object) -> bool:
        """
        Evalúa si el límite de carga es mayor al del otro vehículo
        """
        return not self.__le__(other)

    #Método mayor o igual que
    def __ge__(self, other: object) -> bool:
        """
        Evalúa si el límite de carga es mayor o igual al del otro vehículo
        """
        return not self.__lt__(other)

    #Método para serializar el objeto
    def serialize(self) -> str:
        """
        Serializa el objeto en un string
        """
        vehicle_dict = dict(
            id = self._id,
            payload = self._payload,
        )

        return json.dumps(vehicle_dict)

    #Método para deserializar el objeto
    def deserialize(self, vehicle_json: str) -> None:
        """
        Deserializa el objeto en formato JSON
        """
        vehicle_dict = json.loads(vehicle_json)

        self._id = vehicle_dict["id"]
        self._payload = vehicle_dict["payload"]
    
    #Método para representar el objeto en string
    def __str__(self) -> str:
        res = f"Vehiculo: {self._id}, Limite de carga: {self._payload}\n"
        for shipment in self._shipments:
            res += f"{shipment}\n"
        return res
        
