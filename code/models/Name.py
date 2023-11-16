class Name:
    """
    -Clase Nombre-\n
    clase para definir el nombre de alguna persona, en este caso del cliente\n
    -Atributos\n
    first -> string\n
    last -> string\n
    
    -Métodos\n
    get_first()\n
    get_last()\n
    set_first( first: string )\n
    set_last( last: string )\n
    """
    #Constructor
    def __init__(self, first: str = None, last: str = None) -> None:
        """
        Constructor de la clase Coordenada.

        Puede recibir dos parámetros o en caso de 
        no recibirlos inicializa los atributos en None.
        """
        self._first = first
        self._last = last
    
    #Método get para el primer nombre
    def get_first(self) -> str:
        """
        Retorna el primer nombre 
        """
        return self._first
    
    #Método get para el apellido
    def get_last(self) -> str:
        """
        Retorna el apellido
        """
        return self._last
    
    #Método set para el primer nombre
    def set_first(self, first: str) ->None:
        """
        Establece el primer nombre
        """
        self._fist = first
    
    #Método set para el apellido
    def set_last(self, last: str) ->None:
        """
        Establece el apellido
        """
        self.last = last
    
    #Método igual que
    def __eq__(self, other: object) -> bool:
        """
        Evalúa si los apellidos son iguales
        """
        if isinstance(other, Name):
            return self._last.lower() == other._last.lower()
        
        return False

    #Método diferente que
    def __ne__(self, other: object) -> bool:
        """
        Evalúa si los apellidos son diferentes
        """
        return not self.__eq__(other)
    
    #Método menor que
    def __lt__(self, other: object) -> bool:
        """
        Evalúa si el apellido es menor al de el otro objeto
        """
        if isinstance(other, Name):
            return self._last.lower() < other._last.lower()
        return NotImplemented
    
    #Método menor o igual que
    def __le__(self, other: object) -> bool:
        """
        Evalúa si el apellido es menor o igual al de el otro objeto
        """
        return self.__lt__(other) or self.__eq__(other)
    
    #Método mayor que
    def __gt__(self, other: object) -> bool:
        """
        Evalúa si el apellido es mayor al de el otro objeto
        """
        return not self.__le__(other)
    
    #Método mayor o igual que
    def __ge__(self, other: object) -> bool:
        """
        Evalúa si el apellido es mayor o igual al de el otro objeto
        """
        return not self.__lt__(other)
    
    #Método para representar el objeto en string
    def __str__(self) -> str:
        return f"{self._first} {self._last}"