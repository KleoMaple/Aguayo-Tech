import json

from constants import CLIENTS_PATH

from models.Client import Client
from models.Coordinate import Coordinate
from models.Name import Name

from typing import List

def get_clients()-> List[Client]:

    with open(CLIENTS_PATH, 'r', encoding="UTF-8") as file:
        clients = json.load(file)

    return [map_client(client) for client in clients['clients']]

def map_client(client: Client) -> Client:
    return Client(
                Name(
                    client['nombre'], 
                    client['apellido']
                ), 
                Coordinate(
                    client['coordenada_X'],
                    client['coordenada_Y']
                )
            )
        

def get_clients_names(clients: List[Client]) -> List[str]:
    return [client.get_name().__str__() for client in clients]