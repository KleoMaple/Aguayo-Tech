from models.Coordinate import Coordinate
from models.Vehicle import Vehicle
from models.Shipment import Shipment
from models.Name import Name
from models.Client import Client

"""
    Constantes para utilizar en todo el sistema. En caso de que vean que tienen una 
    variable que su valor no cambiará y que pueden separar de su lógica, pueden declararla aquí.
"""

# FRONTEND

ASSETS_PATH = "assets/"
CLIENTS_PATH = "mocks/clients.json"
ORDERS_PATH = "mocks/orders.json"

# BACKEND

VEHICLE_LIMIT = 25

LIGHT_VEHICLE = Vehicle("camion1", 80)
HEAVY_VEHICLE = Vehicle("camion2", 120)

WAREHOUSE = Coordinate(0, 0)
WAREHOUSE_SHIPMENT = Shipment(Client(Name("Bodega", "Central"), WAREHOUSE))