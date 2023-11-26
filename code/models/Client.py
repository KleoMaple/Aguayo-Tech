from models.Name import Name
from models.Coordinate import Coordinate

import json

class Client:
    """
    ## Clase Cliente\n
    clase para identificar a un cliente por su dirección y nombre

    ### Atributos\n
    name -> Name\n
    address -> Coordinate\n

    ### Métodos\n
    get_name()\n
    get_address()\n
    set_name( name: Name )\n
    set_address( address: Coordinate )\n

    """

    #Constructor
    def __init__(self, name: Name = None, address: Coordinate = None) -> None:
        """
        Constructor de la clase Cliente.

        Puede recibir dos parámetros o en caso de 
        no recibirlos inicializa los atributos en None
        """
        self._name = name
        self._address = address

    #Método get del nombre
    def get_name(self) -> Name:
        """
        Retorna el nombre del cliente
        """
        return self._name
    
    #Método get de la dirección
    def get_address(self) -> Coordinate:
        """
        Retorna la dirección del cliente
        """
        return self._address
    
    #Método set del nombre
    def set_name(self, name: str) -> None:
        """
        Establece el nombre del cliente
        """
        self._name = name
    
    #Método set de la dirección
    def set_address(self, address: Coordinate) ->None:
        """
        Establece la dirección del cliente
        """
        self._address = address
    
    #Método igual que
    def __eq__(self, other: object) -> bool:
        """
        Evalúa si tanto el nombre del cliente como la dirección son iguales
        """
        if isinstance(self, Client):
            return self._name == other._name and self._address == other._address
        
        return False

    #Método diferente que 
    def __ne__(self, other: object) -> bool:
        """
        Evalúa si tanto el nombre del cliente como la dirección son distinto
        """
        return not self.__eq__(other)
    
    #Método menor que
    def __lt__(self, other: object) -> bool:
        """
        Evalúa si tanto el nombre es menor que el de el otro objeto alfabéticamente
        """
        if isinstance(other, Client):
            return self._name < other._name
        
        return NotImplemented
    
    #Método menor o igual que
    def __le__(self, other: object) -> bool:
        """
        Evalúa si tanto el nombre es menor o igual que el de el otro objeto alfabéticamente
        """
        return self.__le__(other) or self.__eq__(other)
    
    #Método mayor que
    def __gt__(self, other: object) -> bool:
        """
        Evalúa si tanto el nombre es mayor que el de el otro objeto alfabéticamente
        """
        return not self.__le__(other)
    
    #Método mayor o igual que
    def __ge__(self, other: object) -> bool:
        """
        Evalúa si tanto el nombre es mayor o igual que el de el otro objeto alfabéticamente
        """
        return not self.__lt__(other)

    #Método para serializar el objeto
    def serialize(self) -> str:
        """
        Serializa el objeto en formato JSON
        """
        client_json = self._name.serialize()[:-1] + ", " + self._address.serialize()[1:]

        return client_json
    
    #Método para deserializar el objeto
    def deserialize(self, client_json: str) -> None:
        """
        Deserializa el objeto en formato JSON
        """
        client_dict = json.loads(client_json)
        self._name = Name(client_dict["first"], client_dict["last"])
        self._address = Coordinate(client_dict["coordinate_X"], client_dict["coordinate_Y"])

    #Método para representar el objeto en string
    def __str__(self) -> str:
        return f"Cliente: {self._name}, Ubicación: {self._address}"