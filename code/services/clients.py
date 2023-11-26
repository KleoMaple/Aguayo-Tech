import json
from constants import CLIENTS_PATH
from models.Client import Client
from models.Coordinate import Coordinate
from models.Name import Name
from typing import List

#Método para obtener los clientes
def get_clients() -> List[Client]:
    """
    Método para obtener los clientes

    ### Retorna:
    - Lista de clientes
    """
    try:
        with open(CLIENTS_PATH, 'r', encoding="UTF-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        # Manejar la excepción si el archivo no existe
        return []

    clients_data = data.get('clients', [])  # Obtener la lista de clientes o una lista vacía si 'clients' no existe
    return [map_client(client) for client in clients_data]

#Método para mapear los clientes
def map_client(client_data: dict) -> Client:
    """
    Recibe un diccionario con los datos de un cliente y retorna una instancia de la clase Client

    ### Recibe como parámetros:
    - client_data: Diccionario con los datos de un cliente

    ### Retorna:
    - Instancia de la clase Client
    """
    return Client(
        Name(client_data['nombre'], client_data['apellido']),
        Coordinate(client_data['coordenada_X'], client_data['coordenada_Y'])
    )

#Método para obtener los nombres de los clientes
def get_clients_names(clients: List[Client]) -> List[str]:
    """
    Recibe una lista de clientes y retorna una lista con los nombres de los clientes

    ### Recibe como parámetros:
    - clients: Lista de clientes

    ### Retorna:
    - Lista de nombres de clientes
    """
    return [client.get_name().__str__() for client in clients]