from models.Shipment import Shipment
from models.Client import Client
from models.Name import Name
from models.Coordinate import Coordinate
from models.Product import Product
from random import randint

weights = [i for i in range(1, 50)]

shipments = [
    Shipment(
        Client(
            Name(f"Client{i}", f"Surname{i}"), 
            Coordinate(i, i*2)
        ),
        Product("Product Name", weights[randint(0, len(weights) - 1)])
    )
    for i in range(1, 61)
]

'''pedido: {
    "Cliente":{
        "first": "askldfjklas",
        "last": "asldkfjklas",
        "coordinate_x": 123,
        "coordinate_y": 123
    },
    "Producto":{
        "name": "askldfjklas",
        "weight": 123
    }
}'''