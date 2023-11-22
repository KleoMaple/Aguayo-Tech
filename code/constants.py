from models.Coordinate import Coordinate
from models.Vehicle import Vehicle
"""
    Constantes para utilizar en todo el sistema. En caso de que vean que tienen una 
    variable que su valor no cambiará y que pueden separar de su lógica, pueden declararla aquí.
"""

# FRONTEND

ASSETS_PATH = "assets/"
CLIENTS_PATH = "mocks/clients.json"

# CONSTANTES BACKEND

VEHICLE_LIMIT = 25

LIGHT_VEHICLE = Vehicle("camion1", 4)
HEAVY_VEHICLE = Vehicle("camion2", 8)

WAREHOUSE = Coordinate(0, 0)

"""
    LIMITES DEL MAPA

                           100
                            |
               NORTH_EAST   |    NORTH_WEST
                            |
                            |
          -100--------------+--------------100
                            |
                            |
              SOUTH_EAST    |    SOUTH_WEST
                            |
                          -100

"""
NORTH_EAST = [Coordinate(-100, 0), Coordinate(0, 100)]
NORTH_WEST = [Coordinate(0, 100), Coordinate(100, 0)]
SOUTH_EAST = [Coordinate(-100, 0), Coordinate(0, -100)]
SOUTH_WEST = [Coordinate(100, 0), Coordinate(0, -100)]
