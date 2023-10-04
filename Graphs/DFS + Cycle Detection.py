from collections import deque


def dfs(node, graph, visited, cycle):
    if node in cycle:
        raise Exception("Cycle Found")

    if node in visited:
        return

    visited.add(node)
    cycle.appendleft(node) # taka slagam cycle detection poprincip ne e chast ot algorituma

    for child in graph[node]:
        dfs(child, graph, visited, cycle)

    cycle.remove(node)
    print(node, end=" ")


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
cycle = deque()

for node in graph:
    dfs(node, graph, visited, cycle)