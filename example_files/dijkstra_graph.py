"""
Dijkstra's Algorithm - Shortest path in weighted graph
"""
import heapq
from collections import defaultdict

def dijkstra(graph, start, end):
    """
    Find shortest path using Dijkstra's algorithm.
    Graph is represented as adjacency list with weights.
    """
    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    distances = {start: 0}
    visited = set()
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        if current_vertex == end:
            return current_dist
        
        # Check neighbors
        for neighbor, weight in graph[current_vertex]:
            if neighbor not in visited:
                new_dist = current_dist + weight
                
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    
    return float('inf')  # No path found


if __name__ == "__main__":
    # Build graph: adjacency list
    graph = defaultdict(list)
    graph['A'] = [('B', 4), ('C', 2)]
    graph['B'] = [('C', 1), ('D', 5)]
    graph['C'] = [('D', 8), ('E', 10)]
    graph['D'] = [('E', 2)]
    
    result = dijkstra(graph, 'A', 'E')
    print(f"Shortest path distance: {result}")
