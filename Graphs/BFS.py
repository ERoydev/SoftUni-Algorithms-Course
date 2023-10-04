from collections import deque


def bfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)
    queue = deque([node])

    while queue:
        current_quene = queue.popleft()
        print(current_quene)

        for child in graph[current_quene]:
            if child not in visited:
                visited.add(child)
                queue.append(child)


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "D": [],
    "E": [],
    "C": ["F", "G"],
    "F": [],
    "G": []
}

visited = set()

for node in graph:
    bfs(node, graph, visited)