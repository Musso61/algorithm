from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        visited.add(start)

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result


def main():
    g = Graph()

    edges = [
        (1, 2), (1, 3),
        (2, 4), (2, 5),
        (3, 6), (3, 7)
    ]

    for u, v in edges:
        g.add_edge(u, v)

    print(g.bfs(1))


if __name__ == "__main__":
    main()
