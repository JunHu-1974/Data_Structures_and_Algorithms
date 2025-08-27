from graph import Graph

def print_path(graph: Graph, predecessors: list[int], source: tuple[int, int], target: tuple[int, int]) -> None:
    path = []
    source_index = graph.vertices.index(source)
    curr = graph.vertices.index(target)
    while curr > 0:
        path.insert(0, str(graph.vertices[curr]))
        curr = predecessors[curr]
        if curr == source_index:
            path.insert(0, str(source))
            curr = -1
    print('->'.join(path))

def bellman_ford(graph: Graph, source: tuple[int, int]) -> tuple[list[int], list[int]]:
    source_index =  graph.vertices.index(source)
    distances = graph.size * [float('inf')]
    distances[source_index] = 0
    predecessors = graph.size * [-1]
    for i in range(graph.size-1):
        for u in range(graph.size):
            for v in range(graph.size):
                if graph.adj_matrix[u][v] != float('inf'):
                    new_distance = distances[u] + graph.adj_matrix[u][v]
                    if new_distance < distances[v]:
                        distances[v] = new_distance
                        predecessors[v] = u
    for u in range(graph.size):
        for v in range(graph.size):
            if graph.adj_matrix[u][v] != float('inf'):
                new_distance = distances[u] + graph.adj_matrix[u][v]
                if new_distance < distances[v]:
                    predecessors = []
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
    distances, predecessors = bellman_ford(graph, (0,1))
    for i,d in enumerate(distances):
        print(graph.vertices[i], distances[i])
    if predecessors:
        print_path(graph, predecessors, (0,1), (2,2))
    else:
        print('Negative weight cycle detected')
    graph.add_edge(3, 1, -3, True)
    distances, predecessors = bellman_ford(graph, (0,1))
    for i,d in enumerate(distances):
        print(graph.vertices[i], distances[i])
    if predecessors:
        print_path(graph, predecessors, (0,1), (2,2))
    else:
        print('Negative weight cycle detected')
    graph.add_edge(3, 1, -9, True)
    distances, predecessors = bellman_ford(graph, (0,1))
    for i,d in enumerate(distances):
        print(graph.vertices[i], distances[i])
    if predecessors:
        print_path(graph, predecessors, (0,1), (2,2))
    else:
        print('Negative weight cycle detected')

if __name__ == '__main__':
    main()