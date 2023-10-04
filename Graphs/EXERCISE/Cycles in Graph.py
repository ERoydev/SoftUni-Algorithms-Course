from collections import deque


def dfs(node, graph, visited, cycle):
    if node in cycle:
        raise Exception

    if node in visited:
        return

    visited.add(node)
    cycle.appendleft(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycle)

    cycle.remove(node)


graph = {}

while True:
    line = input()
    if line == "End":
        break

    node, parent = line.split("-")
    graph[node] = graph.get(node, [])
    graph[parent] = graph.get(parent, [])
    graph[node].append(parent)

visited = set()

try:
    for node in graph:
        cycle = deque()
        dfs(node, graph, visited, cycle)
    print(f"Acyclic: Yes")

except Exception:
    print(f"Acyclic: No")


