import requests

from api import GOOGLE_API_KEY
from dijkstra import dijkstra

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

def get_distance_matrix(api_key, origins, destinations, mode='driving'):
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    
    params = {
        'origins': '|'.join(origins),
        'destinations': '|'.join(destinations),
        'mode': mode,
        'key': api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        return data['rows']
    else:
        return None

def create_graph(api_key, origins, destinations, mode='driving'):
    graph = Graph()

    for origin in origins:
        graph.add_node(origin)

    for destination in destinations:
        graph.add_node(destination)

    distance_matrix = get_distance_matrix(api_key, origins, destinations, mode)

    for i, origin in enumerate(origins):
        for j, destination in enumerate(destinations):
            weight = distance_matrix[i]['elements'][j]['duration']['value']
            graph.add_edge(origin, destination, weight)

    return graph

def calculate_shortest_route(api_key, origins, destinations, mode='driving'):
    graph = create_graph(api_key, origins, destinations, mode)
    shortest_route = dijkstra(graph, origins[0]) 

    return shortest_route

api_key = GOOGLE_API_KEY
origins = ["New York, NY", "Los Angeles, CA", "Chicago, IL"]
destinations = ["San Francisco, CA", "Seattle, WA", "Miami, FL"]

shortest_route = calculate_shortest_route(api_key, origins, destinations)

print("Shortest route:")
for node, distance in shortest_route.items():
    print(f"To {node}: {distance} seconds")
