## 8. Bellman-Ford Algorithm
import math

def bellman_ford(graph: list[list[int]], source: int) -> tuple[list[int], bool]:
    """
    Time Complexity: O(V * E)
    Space Complexity: O(V)
    """
    V = len(graph)
    distance = [math.inf] * V
    distance[source] = 0

    for _ in range(V - 1):
        for u in range(V):
            for v in range(V):
                if graph[u][v] != math.inf and distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]

    for u in range(V):
        for v in range(V):
            if graph[u][v] != math.inf and distance[u] + graph[u][v] < distance[v]:
                return distance, True

    return distance, False

def test_bellman_ford():
    INF = float('inf')
    graph = [
        [0,     6, INF,    7],
        [INF,   0,   5,    8],
        [INF,  -2,   0,  INF],
        [INF, INF,  -3,    0]
    ]
    distances, has_negative_cycle = bellman_ford(graph, 0)
    return distances, has_negative_cycle

print(test_bellman_ford())