from collections import deque


def dfs(node, graph, visited, cycles, sorted_nodes):
    if node in cycles:
        raise Exception("Cycle has been detected. Invalid topological sorting.")

    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles, sorted_nodes)

    cycles.remove(node)
    sorted_nodes.appendleft(node)


n = int(input())
graph = {}

for idx in range(n):
    line = input().split("->")
    node = line[0].strip()
    children = line[1].strip().split(", ") if line[1] else []

    graph[node] = children

visited = set()
cycles = set()

sorted_nodes = deque()
for node in graph:
    dfs(node, graph, visited, cycles, sorted_nodes)

print(*sorted_nodes, sep=" ")