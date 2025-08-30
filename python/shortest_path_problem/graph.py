from typing import Optional

class Graph(object):
    def __init__(self, size: int = 10):
        self.size = size
        self.vertices = size * [None]
        self.neighbors = size * [None]
        self.adj_matrix = [size * [float('inf')] for i in range(size)]
    
    def add_vertex(self, index: int, data: Optional[tuple[int, int]]) -> None:
        if index < 0 or index >= self.size:
            return
        if data is None:
            if self.neighbors:
                return
            else:
                self.vertices[index] = None
                self.neighbors[index] = None
        else:
            self.vertices[index] = data
            if self.neighbors[index] is None:
                self.neighbors[index] = set()

    def add_edge(self, start: int, end: int, weight: int, directed: bool) -> None:
        if start < 0 or start >= self.size or self.vertices[start] is None:
            return
        if end < 0 or end >= self.size or self.vertices[end] is None:
            return
        if weight == float('inf'):
            if end in self.neighbors[start]:
                self.neighbors[start].remove(end)
            if not directed:
                if start in self.neighbors[end]:
                    self.neighbors[end].remove(start)
        else:
            self.neighbors[start].add(end)
            if not directed:
                self.neighbors[end].add(start)
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
        print(graph.vertices[i], graph.adj_matrix[i], graph.neighbors[i])

if __name__ == '__main__':
    main()