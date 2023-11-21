from mocks.shipments import shipments

from services.distances import filter_shipments, get_addresses
from services.graph import create_graph, draw_graph


def main():

    shipments_beyond, shipments_within = filter_shipments(shipments)

    distances_beyond = get_addresses(shipments_beyond)
    distances_within = get_addresses(shipments_within)

    g_beyond = create_graph(distances_beyond)
    g_within = create_graph(distances_within)

    draw_graph(g_beyond)
    draw_graph(g_within)
    

if __name__ == '__main__':
    main()
    