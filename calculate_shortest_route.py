from dijkstra import dijkstra
from create_graph import create_graph

def calculate_shortest_route(api_key, origins, destinations, mode='driving'):
    graph = create_graph(api_key, origins, destinations, mode)
    shortest_route = dijkstra(graph, origins[0]) 

    return shortest_route