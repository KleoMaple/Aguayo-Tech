from math import sqrt
import json

class Coordinate:
    """
    ## Clase coordenada\n
    clase para representar direcciones en el sistema

    ### Atributos\n
    x -> float\n
    y -> float\n

    ### Métodos\n
    get_x()\n
    get_y()\n
    set_x( x: float )\n
    set_y( y: float )\n
    get_distance()\n
    """
    #Constructor
    def __init__(self, x: float = None, y: float = None) -> None:
        """
        Constructor de la clase Coordenada.

        Puede recibir dos parámetros o en caso de 
        no recibirlos inicializa los atributos en None.
        """
        self._x = x
        self._y = y
    
    #Método get de la coordenada X
    def get_x(self) -> float:
        """
        Retorna la coordenada en X
        """
        return self._x
    
    #Método get de la coordenada Y
    def get_y(self) -> float:
        """
        Retorna la coordenada en Y
        """
        return self._y
    
    #Método set de la coordenada X
    def set_x(self, x: float) -> None:
        """
        Establece la coordenada en X
        """
        self._x = x
    
    #Método set de la coordenada Y
    def set_y(self, y: float) -> None:
        """
        Establece la coordenada en Y
        """
        self._y = y
    
    #Método para obtener la distancia respecto al origen
    def get_distance(self) -> int:
        """
        Obtiene la distancia respecto al origen
        """
        return int(sqrt(self._x**2 + self._y**2))

    #Método para obtener la distancia respecto a otro objeto
    def get_distance_to(self, other: object) -> int:
        """
        Obtiene la distancia respecto a otro objeto
        """
        if isinstance(other, Coordinate):
            return int(sqrt((self._x - other.get_x())**2 + (self._y - other.get_y())**2))
        return NotImplemented

    #Método para obtener las coordenadas en forma de tupla
    def get_point(self) -> tuple:
        """
        Retorna las coordenadas en forma de tupla
        """
        return self._x, self._y
    
    #Método igual que
    def __eq__(self, other: object) -> bool:
        """
        Evalúa si las distancias respecto al origen son iguales
        """
        if isinstance(other, Coordinate):
            return self.get_distance() == other.get_distance()
        
        return False

    #Método diferente que
    def __ne__(self, other: object) -> bool:
        """
        Evalúa si las distancias respecto al origen son distintas
        """
        return not self.__eq__(other)
    
    #Método menor que
    def __lt__(self, other: object) -> bool:
        """
        Evalúa si la distancia al origen es menor respecto a la del otro objecto
        """
        if isinstance(other, Coordinate):
            return self.get_distance() < other.get_distance()
        return NotImplemented

    #Método menor o igual que
    def __le__(self, other: object) -> bool:
        """
        Evalúa si la distancia al origen es menor o igual respecto a la del otro objecto
        """
        return self.__eq__(other) or self.__lt__(other)

    #Método mayor que
    def __gt__(self, other: object) -> bool:
        """
        Evalúa si la distancia al origen es mayor respecto a la del otro objecto
        """
        return not self.__le__(other)
    
    #Método mayor o igual que
    def __ge__(self, other: object) -> bool:
        """
        Evalúa si la distancia al origen es mayor o igual respecto a la del otro objecto
        """
        return not self.__lt__(other)

    #Método para serializar el objeto
    def serialize(self) -> str:
        """
        Serializa el objeto en formato JSON
        """
        coordinate_dict = dict(
            coordinate_X = self._x,
            coordinate_Y = self._y
        )

        return json.dumps(coordinate_dict)
    
    #Método para deserializar el objeto
    def deserialize(self, coordinate_json: str):
        """
        Deserializa el objeto en formato JSON
        """
        coordinate_dict = json.loads(coordinate_json)

        self._x = coordinate_dict["coordinate_X"]
        self._y = coordinate_dict["coordinate_Y"]

    
    #Método para representar el objeto en string
    def __str__(self) -> str:
        return f"(X {self._x}, Y {self._y})"