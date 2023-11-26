from models.Shipment import Shipment    

from typing import List

class Route:
    """
    ## Clase que representa una ruta. Contiene una lista de pedidos.

    ### Atributos\n
    - shipments -> list[Shipment]

    ### Métodos
    - get_shipments()
    - set_shipments(shipments: List[Shipment])

    """

    #Constructor
    def __init__(self, shipments: List[Shipment] = []) -> None:
        """
        Constructor de la clase Route.
        
        Puede recibir un parámetro o en caso de
        no recibirlo inicializa el atributo en una lista vacía
        """
        self._shipments = shipments
    
    #Método get de los pedidos
    def get_shipments(self) -> List[Shipment]: 
        """
        retorna los pedidos de la ruta
        """
        return self._shipments

    #Método set de los pedidos
    def set_shipments(self, shipments: List[Shipment]) -> None:
        """
        Establece los pedidos de la ruta
        """
        self._shipments = shipments

    #Método para representar le objeto con un string
    def __str__(self) -> str:
        str_res = ""
        for shipment in self._shipments:
            str_res += f"{shipment}\n"

        return str_res
    