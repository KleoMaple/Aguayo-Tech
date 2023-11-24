from models.Shipment import Shipment
from models.Client import Client
from models.Name import Name
from models.Coordinate import Coordinate
from models.Product import Product

shipments = [
    Shipment(
        Client(
            Name(f"Client{i}", f"Surname{i}"), 
            Coordinate(i, i*2)
        ),
        Product("Product Name", i)
    )
    for i in range(1, 21)
]