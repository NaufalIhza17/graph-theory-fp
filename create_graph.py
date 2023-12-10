from get_distance_matrix import get_distance_matrix 
from graph import Graph

def create_graph(api_key, origins, destinations, mode='driving'):
    graph = Graph()

    for origin in origins:
        graph.add_node(origin)

    for destination in destinations:
        graph.add_node(destination)

    distance_matrix = get_distance_matrix(api_key, origins, destinations, mode)

    for i, origin in enumerate(origins):
        for j, destination in enumerate(destinations):
            distance = distance_matrix[i]['elements'][j]['distance']['value']
            time = distance_matrix[i]['elements'][j]['duration']['value']
            graph.add_edge(origin, destination, {'distance': distance, 'time': time})

    return graph