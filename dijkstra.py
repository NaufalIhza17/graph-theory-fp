import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    visited = set()
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0

    while heap:
        (current_weight, current_node) = heapq.heappop(heap)

        if current_node in visited:
            continue

        visited.add(current_node)

        for (neighbor, weight) in graph.edges[current_node]:
            if neighbor not in visited:
                total_weight = current_weight + weight
                if total_weight < distances[neighbor]:
                    distances[neighbor] = total_weight
                    heapq.heappush(heap, (total_weight, neighbor))

    return distances