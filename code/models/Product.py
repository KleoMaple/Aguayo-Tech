class Product:
    """
    -Clase Producto-\n
    clase para definir los productos que se enviaran

    -Atributos\n
    name -> string\n
    weight -> int\n

    -Métodos\n
    get_name()\n
    get_weight()\n
    set_name( name: string )\n
    set_weight( weight: int )\n
    """

    #Constructor
    def __init__(self, name: str = None, weight: int = None) -> None:
        """
        Constructor de la clase Productos.

        Puede recibir dos parámetros o en caso de 
        no recibirlos inicializa los atributos en None.
        """
        self._name = name
        self._weight = weight

    #Método get del nombre
    def get_name(self) -> str:
        """
        Retorna el nombre del producto
        """
        return self._name
    
    #Método get del peso 
    def get_weight(self) -> int:
        """
        Retorna el peso que ocupa un producto
        """
        return self._weight

    #Método set del nombre
    def set_name(self, name: str) ->None:
        """
        Establece el nombre de un producto
        """
        self._name = name
    
    #Método set del peso
    def set_weight(self, weight: int) -> None:
        """
        Establece el peso que ocupa un producto
        """
        self._weight = weight
    
    #Método igual que 
    def __eq__(self, other: object) -> bool:
        """
        Compara si los pesos que ocupan los dos productos son iguales
        """
        if isinstance(other, Product):
            return self.weight == other.weight
        return False
    
    #Método diferente que 
    def __ne__(self, other: object) -> bool:
        """
        Compara si los pesos que ocupan los dos productos son distintos
        """
        return not self.__eq__(other)
    
    #Método menor que
    def __lt__(self, other: object) -> bool:
        """
        Compara si el peso que ocupa el producto es menor que el de el otro objeto
        """
        if isinstance(other, Product):
            return self._weight < other.weight
        
        return NotImplemented

    #Método menor o igual que
    def __le__(self, other: object) -> bool:
        """
        Compara si el peso que ocupa el producto es menor o igual que el de el otro objeto
        """
        return self.__lt__(other) or self.__eq__(other)
    
    #Método mayor que
    def __gt__(self, other: object) -> bool:
        """
        Compara si el peso que ocupa el producto es mayor que el de el otro objeto
        """
        return not self.__le__(other)
    
    #Método mayor o igual que
    def __ge__(self, other: object) -> bool:
        """
        Compara si el peso que ocupa el producto es mayor o igual que el de el otro objeto
        """
        return not self.__lt__(other)

    #Método para representar el objeto en string
    def __str__(self) -> str:
        return f"Producto: {self._name}, Peso necesario: {self._weight}"