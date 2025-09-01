from collections import deque
from graph import Graph
import heapq

def print_path(graph: Graph, predecessors: list[int], source: tuple[int, int], target: tuple[int, int]) -> None:
    path = deque()
    source_index = graph.vertices.index(source)
    curr = graph.vertices.index(target)
    while curr > 0:
        path.appendleft(str(graph.vertices[curr]))
        curr = predecessors[curr]
        if curr == source_index:
            path.appendleft(str(source))
            curr = -1
    print('->'.join(path))

def dijkstra_priority_queue(graph: Graph, source: tuple[int, int]) -> tuple[list[int], list[int]]:
    source_index =  graph.vertices.index(source)
    distances = graph.size * [float('inf')]
    distances[source_index] = 0
    predecessors = graph.size * [-1]

    unvisited = set(list(range(graph.size)))
    priority_queue = [(0,source_index)]
    while unvisited and priority_queue:
        print(priority_queue)
        dist,u = heapq.heappop(priority_queue)
        if u in unvisited:
            for v in graph.neighbors[u]:
                if v in unvisited:
                    new_distance = distances[u] + graph.adj_matrix[u][v]
                    if new_distance < distances[v]:
                        distances[v] = new_distance
                        predecessors[v] = u
                        heapq.heappush(priority_queue, (distances[v],v))
            unvisited.remove(u)
    return distances, predecessors

def main() -> None:
    graph = Graph(7)
    graph.add_vertex(0,(0,1))
    graph.add_vertex(1,(0,2))
    graph.add_vertex(2,(1,0))
    graph.add_vertex(3,(1,1))
    graph.add_vertex(4,(1,2))
    graph.add_vertex(5,(2,0))
    graph.add_vertex(6,(2,2))
    graph.add_edge(0, 1, 1, True)
    graph.add_edge(0, 3, 2, True)
    graph.add_edge(1, 4, 5, True)
    graph.add_edge(2, 3, 1, False)
    graph.add_edge(3, 4, 3, False)
    graph.add_edge(2, 5, 1, False)
    graph.add_edge(3, 5, 3, False)
    graph.add_edge(3, 6, 6, False)
    graph.add_edge(4, 6, 1, False)
    graph.add_edge(5, 6, 5, False)

    graph.add_edge(3, 1, 1, True)
    distances, predecessors = dijkstra_priority_queue(graph, (0,1))
    for i,d in enumerate(distances):
        print(graph.vertices[i], distances[i])
    print_path(graph, predecessors, (0,1), (2,2))
    graph.add_edge(3, 1, -2, True)
    distances, predecessors = dijkstra_priority_queue(graph, (0,1))
    for i,d in enumerate(distances):
        print(graph.vertices[i], distances[i])
    print_path(graph, predecessors, (0,1), (2,2))
    graph.add_edge(3, 1, -9, True)
    distances, predecessors = dijkstra_priority_queue(graph, (0,1))
    for i,d in enumerate(distances):
        print(graph.vertices[i], distances[i])
    print_path(graph, predecessors, (0,1), (2,2))

if __name__ == '__main__':
    main()