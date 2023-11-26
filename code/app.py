#from frontend.GUI import main_win

from models.Coordinate import Coordinate
from models.Name import Name
from models.Shipment import Shipment
from models.Product import Product
from models.Client import Client

from constants import LIGHT_VEHICLE

def main():
    #main_win.mainloop()
    coordenada1 = Coordinate(43, 66)
    name1 = Name("Juan", "Perez")
    producto1 = Product("Television", 40)
    client1 = Client(name1, coordenada1)
    shipment1 = Shipment(client1, producto1)


    coordenada_json = coordenada1.serialize()
    name_json = name1.serialize()
    client_json = client1.serialize()
    vehicle_json = LIGHT_VEHICLE.serialize()
    shipment_json = shipment1.serialize()

    print(shipment_json)

    shipment2 = Shipment()

    shipment2.deserialize(shipment_json)

    print(shipment2)
    # coordenada2 = Coordinate()
    # name2 = Name()
    # client2 = Client()
    
    # coordenada2.deserialize(coordenada_json)
    # name2.deserialize(name_json)
    # client2.deserialize(client_json)

    with open("mocks/json_test.json", "w") as file:
        file.write(shipment_json)
        file.close()
        
    # print(coordenada2)
    # print(name2)
    # print(client2)

if __name__ == '__main__':
    main()