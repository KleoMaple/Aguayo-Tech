from models.Shipment import Shipment
from models.Client import Client
from models.Name import Name
from models.Coordinate import Coordinate
from models.Product import Product

from typing import List

shipments: List[Shipment] = [
    Shipment(
        Client(
            Name("Juan", "Perez"), 
            Coordinate(69, 7)
        ),
        Product("Coca Cola", 1)
    ),
    Shipment(
        Client(
            Name("Luis", "Avila"), 
            Coordinate(35, 10)
        ),
        Product("Coca Cola", 1)
    ),
    Shipment(
        Client(
            Name("Maria", "Lopez"), 
            Coordinate(10, 10)
        ),
        Product("Coca Cola", 1)
    ),
    Shipment(
        Client(
            Name("Jose", "Garcia"), 
            Coordinate(79, -88)
        ),
        Product("Coca Cola", 1)
    ),
    Shipment(
        Client(
            Name("Carla", "Fernandez"), 
            Coordinate(4, 15)
        ),
        Product("Coca Cola", 1)
    ),
]