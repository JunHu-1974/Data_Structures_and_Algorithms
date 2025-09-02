from graph import Graph

def print_path(graph: Graph, predecessors: list[int], source: tuple[int, int], target: tuple[int, int]) -> None:
    path = []
    source_index = graph.vertices.index(source)
    curr = graph.vertices.index(target)
    while curr >= 0:
        path.insert(0, str(graph.vertices[curr]))
        if curr == source_index:
            curr = -1
        elif path[0] in path[1:]:
            path.insert(0, '')
            curr = -1
        else:
            curr = predecessors[curr]
    print('->'.join(path))

def bellman_ford(graph: Graph, source: tuple[int, int]) -> tuple[list[int], list[int]]:
    source_index =  graph.vertices.index(source)
    distances = graph.size * [float('inf')]
    distances[source_index] = 0
    predecessors = graph.size * [-1]

    open_list = set([source_index])
    relax_count = 0
    while open_list and relax_count < graph.size:
        open_list.clear()
        for u in range(graph.size):
            for v in graph.neighbors[u]:
                new_distance = distances[u] + graph.adj_matrix[u][v]
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    predecessors[v] = u
                    if not v in open_list:
                        open_list.add(v)
        relax_count += 1
    if relax_count == graph.size:
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
    graph.add_edge(3, 4, 2, False)
    graph.add_edge(2, 5, 1, False)
    graph.add_edge(3, 5, 3, False)
    graph.add_edge(3, 6, 6, False)
    graph.add_edge(4, 6, 1, False)
    graph.add_edge(5, 6, 5, False)

    source = (0,1)
    target = (2,2)

    graph.add_edge(3, 1, 2, True)
    distances, predecessors = bellman_ford(graph, source)
    for i,d in enumerate(distances):
        print(graph.vertices[i], distances[i])
    if predecessors:
        print_path(graph, predecessors, source, target)
    else:
        print('Negative weight cycle detected')
    graph.add_edge(3, 1, -4, True)
    distances, predecessors = bellman_ford(graph, source)
    for i,d in enumerate(distances):
        print(graph.vertices[i], distances[i])
    if predecessors:
        print_path(graph, predecessors, source, target)
    else:
        print('Negative weight cycle detected')
    graph.add_edge(3, 1, -8, True)
    distances, predecessors = bellman_ford(graph, source)
    for i,d in enumerate(distances):
        print(graph.vertices[i], distances[i])
    if predecessors:
        print_path(graph, predecessors, source, target)
    else:
        print('Negative weight cycle detected')

if __name__ == '__main__':
    main()