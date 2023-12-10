import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    visited = set()
    distances = {node: {'distance': float('infinity'), 'time': float('infinity')} for node in graph.nodes}
    distances[start] = {'distance': 0, 'time': 0}

    while heap:
        (current_weight, current_node) = heapq.heappop(heap)

        if current_node in visited:
            continue

        visited.add(current_node)

        for (neighbor, weight) in graph.edges[current_node]:
            if neighbor not in visited:
                total_weight = current_weight + weight['distance']
                total_time = distances[current_node]['time'] + weight['time']

                if total_weight < distances[neighbor]['distance']:
                    distances[neighbor] = {'distance': total_weight, 'time': total_time}
                    heapq.heappush(heap, (total_weight, neighbor))

    return distances