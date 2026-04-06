
# ---------------- ЗАДАЧА 1 ----------------
# Граф (список смежности)
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}

print("Исходный граф:", graph)


# ---------------- ЗАДАЧА 2 ----------------
# Добавляем новую вершину
def add_vertex(graph, vertex, connections):
    graph[vertex] = connections
    for v in connections:
        graph[v].append(vertex)


add_vertex(graph, "F", ["A", "E"])
print("После добавления вершины F:", graph)


# ---------------- ЗАДАЧА 3 ----------------
# Функция для вывода соседей
def get_neighbors(graph, node):
    return graph.get(node, [])


print("Соседи вершины A:", get_neighbors(graph, "A"))


# ---------------- ЗАДАЧА 4 ----------------
# DFS (рекурсивный)
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


# ---------------- ЗАДАЧА 5 ----------------
# DFS через стек
def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))

    return visited


# ---------------- ЗАДАЧА 6 ----------------
# BFS через очередь
from collections import deque


def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


# ---------------- ЗАДАЧА 7 ----------------
# Программа с вводом
def run_traversal(graph):
    start = input("\nВведите стартовую вершину: ")

    if start not in graph:
        print("Такой вершины нет!")
        return

    print("\nDFS (рекурсивно):")
    dfs_recursive(graph, start)

    print("\nDFS (через стек):")
    dfs_stack(graph, start)

    print("\nBFS:")
    bfs(graph, start)


# ---------------- ЗАДАЧА 8 ----------------
# Проверка существования пути
def path_exists(graph, start, end):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

    return False


# ---------------- ЗАДАЧА 9 ----------------
# Количество достижимых вершин
def reachable_count(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

    return len(visited)


# ---------------- ЗАДАЧА 10 ----------------
# Кратчайший путь (BFS)
def shortest_path(graph, start, end):
    from collections import deque

    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


# ---------------- ПРОВЕРКА ВСЕГО ----------------
print("\nDFS (рекурсивно) от A:")
dfs_recursive(graph, "A")

print("\nDFS (стек) от A:")
dfs_stack(graph, "A")

print("\nBFS от A:")
bfs(graph, "A")

print("\n\nПуть между A и E:", path_exists(graph, "A", "E"))

print("Количество достижимых вершин из A:", reachable_count(graph, "A"))

print("Кратчайший путь от A до E:", shortest_path(graph, "A", "E"))