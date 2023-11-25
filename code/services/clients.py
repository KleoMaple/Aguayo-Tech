import json
from constants import CLIENTS_PATH
from models.Client import Client
from models.Coordinate import Coordinate
from models.Name import Name
from typing import List

def get_clients() -> List[Client]:
    try:
        with open(CLIENTS_PATH, 'r', encoding="UTF-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        # Manejar la excepción si el archivo no existe
        return []

    clients_data = data.get('clients', [])  # Obtener la lista de clientes o una lista vacía si 'clients' no existe
    return [map_client(client) for client in clients_data]

def map_client(client_data: dict) -> Client:
    return Client(
        Name(client_data['nombre'], client_data['apellido']),
        Coordinate(client_data['coordenada_X'], client_data['coordenada_Y'])
    )

def get_clients_names(clients: List[Client]) -> List[str]:
    return [client.get_name().__str__() for client in clients]