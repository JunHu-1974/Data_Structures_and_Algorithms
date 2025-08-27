class Graph(object):
    def __init__(self, size: int = 10):
        self.size = size
        self.adj_matrix = [size * [float('inf')] for i in range(size)]
        self.vertices = size * [None]
    
    def add_vertex(self, index: int, data: tuple[int, int]) -> None:
        if index >= 0 and index < self.size:
            self.vertices[index] = data

    def add_edge(self, start: int, end: int, weight: int, directed: bool) -> None:
        if start >= 0 and start < self.size and end >= 0 and end < self.size:
            self.adj_matrix[start][end] = weight
            if not directed:
                self.adj_matrix[end][start] = weight

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
    for i in range(graph.size):
        print(graph.vertices[i], graph.adj_matrix[i])

if __name__ == '__main__':
    main()