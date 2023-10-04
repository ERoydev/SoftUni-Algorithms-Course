def dfs(node, graph, visited, connected):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, connected)

    connected.append(node)


n = int(input())

graph = []

for i in range(n):
    graph.append([int(x) for x in input().split()])

visited = [False] * len(graph)

for node in range(len(graph)):
    if visited[node]:
        continue
    connected = []
    dfs(node, graph, visited, connected)
    print(f"Connected component: {' '.join(str(x) for x in connected)}")