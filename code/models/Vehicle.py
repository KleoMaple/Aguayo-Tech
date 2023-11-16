class Vehicle:
    """
    -Clase Vehiculo-\n
    clase para definir los vehículos que usarán las rutas

    -Atributos\n
    id -> string \n
    payload -> int\n

    -Métodos\n
    get_id()\n
    get_payload()\n
    set_id( id: string )\n
    set_payload( payload: int )\n
    """

    #Constructor
    def __init__(self, id: str = None, payload: int = None) -> None:
        """
        Constructor de la clase vehículo.

        Puede recibir dos parámetros o en caso de 
        no recibirlos inicializa los atributos en None
        """
        self._id = id
        self._payload = payload

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

    #Método para representar el objeto en string
    def __str__(self) -> str:
        return f"Vehiculo: {self._id}, Limite de carga: {self._payload}"
