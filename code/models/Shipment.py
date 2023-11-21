from models.Client import Client
from models.Product import Product

class Shipment:
    def __init__(self, client: Client, product: Product) -> None:
        self._client = client
        self._product = product

    
    def get_client(self) -> Client:
        return self._client
    
    def get_product(self) -> Product:
        return self._product
    
    def set_client(self, client: Client) -> None:
        self._client = client

    def set_product(self, product: Product) -> None:
        self._product = product
    
    def __str__(self) -> str:
        return f"Cliente: {self._client.get_name()} - Producto: {self._product.get_name()}"
    