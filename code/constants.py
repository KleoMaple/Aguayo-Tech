from models.Coordinate import Coordinate
from models.Vehicle import Vehicle
"""
    Constantes para utilizar en todo el sistema. En caso de que vean que tienen una 
    variable que su valor no cambiará y que pueden separar de su lógica, pueden declararla aquí.
"""

# FRONTEND

ASSETS_PATH = "assets/"
CLIENTS_PATH = "mocks/clients.json"

# BACKEND

VEHICLE_LIMIT = 25

LIGHT_VEHICLE = Vehicle("camion1", 80)
HEAVY_VEHICLE = Vehicle("camion2", 80)

WAREHOUSE = Coordinate(0, 0)