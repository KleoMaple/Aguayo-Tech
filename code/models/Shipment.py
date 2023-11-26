from models.Client import Client
from models.Product import Product
from models.Name import Name
from models.Coordinate import Coordinate    

import json
class Shipment:
    """
    ## Clase Envío\n
    clase para definir los envíos que se realizarán

    ### Atributos\n
    - client -> Client\n
    - product -> Product\n

    ### Métodos\n
    - get_client()\n
    - get_product()\n
    - set_client( client: Client )\n
    - set_product( product: Product )\n

    """
    #Constructor
    def __init__(self, client: Client = Client(), product: Product = None) -> None:
        """
        Contructor de la clase Envío.

        Puede recibir dos parámetros o en caso de
        no recibirlos inicializa los atributos en None.
        """
        self._client = client
        self._product = product

    #Método get del cliente
    def get_client(self) -> Client:
        """
        Retorna el cliente del envío
        """
        return self._client
    
    #Método get del producto
    def get_product(self) -> Product:
        """
        Retorna el producto del envío
        """
        return self._product
    
    #Método set del cliente
    def set_client(self, client: Client) -> None:
        """
        Establece el cliente del envío
        """
        self._client = client

    #Método set del producto
    def set_product(self, product: Product) -> None:
        """
        Establece el producto del envío
        """
        self._product = product
    
    #Método para serializar el objeto
    def serialize(self) -> str:
        """
        Serializa el objeto para poder ser guardado en un archivo JSON
        """
        shipment_json = self._client.serialize()[:-1] + ", " + self._product.serialize()[1:]

        return shipment_json
    
    #Método para deserializar el objeto
    def deserialize(self, shipment_dict: dict) -> None:
        """
        Deserializa el objeto para poder ser leído desde un archivo JSON
        """
        
        client_name = Name(shipment_dict["first"], shipment_dict["last"])
        client_address = Coordinate(shipment_dict["coordinate_X"], shipment_dict["coordinate_Y"])

        self._client = Client(client_name, client_address)
        self._product = Product(shipment_dict["product_name"], shipment_dict["weight"])

    #Método para representar el objeto como un string
    def __str__(self) -> str:
        if not self._product:
            return f"Cliente: {self._client.get_name()}, Dirección: {self._client.get_address()}"
        
        return f"Cliente: {self._client.get_name()}, Dirección: {self._client.get_address()} - Producto: {self._product.get_name()}, Peso: {self._product.get_weight()} kg"
    