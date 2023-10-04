from collections import deque
# Bellman-Ford Algorithm


def find_path(element):
    path = deque()
    node = destination
    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(*path, sep=' ')
    return element


def find_negative_cycle():
    for edge in graph:
        node, destination, weight = edge
        new_distance = distance[node] + weight
        if new_distance < distance[destination]:
            return True

    return False


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append((source, destination, weight))

source = int(input())
destination = int(input())

distance = [float('inf')] * (nodes + 1)
parent = [None] * (nodes + 1)
distance[source] = 0

for i in range(edges - 1):
    updated = False
    for node, end, weight in graph:

        if distance[end] == float('inf'):
            distance[end] = distance[node] + weight
            parent[end] = node
            continue

        new_distance = distance[node] + weight

        if new_distance < distance[end]:
            distance[end] = new_distance
            parent[end] = node
            updated = True

    if not updated:
        break

if find_negative_cycle():
    print(f"Undefined")

else:
    print(find_path(distance[destination]))


