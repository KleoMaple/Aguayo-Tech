class Product:
    """
    -Clase Producto-\n
    clase para definir los productos que se enviaran

    -Atributos\n
    name -> string\n
    space -> int\n

    -Métodos\n
    get_name()\n
    get_space()\n
    set_name( name: string )\n
    set_space( space: int )\n
    """

    #Constructor
    def __init__(self, name: str = None, space: int = None) -> None:
        """
        Constructor de la clase Productos.

        Puede recibir dos parámetros o en caso de 
        no recibirlos inicializa los atributos en None.
        """
        self._name = name
        self._space = space

    #Método get del nombre
    def get_name(self) -> str:
        """
        Retorna el nombre del producto
        """
        return self._name
    
    #Método get del espacio 
    def get_space(self) -> int:
        """
        Retorna el espacio que ocupa un producto
        """
        return self._space

    #Método set del nombre
    def set_name(self, name: str) ->None:
        """
        Establece el nombre de un producto
        """
        self._name = name
    
    #Método set del espacio
    def set_space(self, space: int) -> None:
        """
        Establece el espacio que ocupa un producto
        """
        self._space = space
    
    #Método igual que 
    def __eq__(self, other: object) -> bool:
        """
        Compara si los espacios que ocupan los dos productos son iguales
        """
        if isinstance(other, Product):
            return self.space == other.space
        return False
    
    #Método diferente que 
    def __ne__(self, other: object) -> bool:
        """
        Compara si los espacios que ocupan los dos productos son distintos
        """
        return not self.__eq__(other)
    
    #Método menor que
    def __lt__(self, other: object) -> bool:
        """
        Compara si el espacio que ocupa el producto es menor que el de el otro objeto
        """
        if isinstance(other, Product):
            return self._space < other.space
        
        return NotImplemented

    #Método menor o igual que
    def __le__(self, other: object) -> bool:
        """
        Compara si el espacio que ocupa el producto es menor o igual que el de el otro objeto
        """
        return self.__lt__(other) or self.__eq__(other)
    
    #Método mayor que
    def __gt__(self, other: object) -> bool:
        """
        Compara si el espacio que ocupa el producto es mayor que el de el otro objeto
        """
        return not self.__le__(other)
    
    #Método mayor o igual que
    def __ge__(self, other: object) -> bool:
        """
        Compara si el espacio que ocupa el producto es mayor o igual que el de el otro objeto
        """
        return not self.__lt__(other)

    #Método para representar el objeto en string
    def __str__(self) -> str:
        return f"Producto: {self._name}, Espacio necesario: {self._space}"