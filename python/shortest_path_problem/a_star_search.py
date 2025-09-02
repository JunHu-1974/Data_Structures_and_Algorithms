import heapq
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

def a_star_search(graph: Graph, source: tuple[int, int], target: tuple[int, int], heuristics: list[int]) -> tuple[list[int], list[int]]:
    source_index =  graph.vertices.index(source)
    distances = graph.size * [float('inf')]
    distances[source_index] = 0
    predecessors = graph.size * [-1]

    open_queue = [(0+heuristics[source_index],source_index)]
    closed_list = set()
    while open_queue:
        _,u = heapq.heappop(open_queue)
        # only correct if heuristics are admissible
        if u == graph.vertices.index(target):
            break
        elif not u in closed_list:
            closed_list.add(u)
            for v in graph.neighbors[u]:
                new_distance = distances[u] + graph.adj_matrix[u][v]
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    predecessors[v] = u
                    heapq.heappush(open_queue, (distances[v]+heuristics[v],v))
                    # revisit v if heuristics are inconsistent
                    if v in closed_list:
                        closed_list.remove(v)
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
    heuristics = graph.size * [0]
    for i in range(graph.size):
        heuristics[i] = abs(graph.vertices[i][0] - target[0]) + abs(graph.vertices[i][1] - target[1])

    graph.add_edge(3, 1, 2, True)
    distances, predecessors = a_star_search(graph, source, target, heuristics)
    for i,d in enumerate(distances):
        print(graph.vertices[i], distances[i])
    print_path(graph, predecessors, source, target)
    graph.add_edge(3, 1, -4, True)
    distances, predecessors = a_star_search(graph, source, target, heuristics)
    for i,d in enumerate(distances):
        print(graph.vertices[i], distances[i])
    print_path(graph, predecessors, source, target)
    graph.add_edge(3, 1, -8, True)
    distances, predecessors = a_star_search(graph, source, target, heuristics)
    for i,d in enumerate(distances):
        print(graph.vertices[i], distances[i])
    print_path(graph, predecessors, source, target)

if __name__ == '__main__':
    main()