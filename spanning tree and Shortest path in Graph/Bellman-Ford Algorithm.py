from collections import deque


def find_negative_cycle():
    for edge in edges:
        node, destination, weight = edge
        new_destination = weight + distance[node]
        if new_destination < distance[destination]:
            return True

    return False


def find_path(element):
    path = deque()
    node = target

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(*path, sep=' ')
    return element


def find_destinations():
    distance = [float('inf')] * (nodes + 1)
    parent = [None] * (nodes + 1)
    distance[start] = 0

    for i in range(nodes - 1):
        updated = False
        for edge in edges:
            node, destination, weight = edge

            if distance[destination] == float('inf'):
                parent[destination] = node
                distance[destination] = weight + distance[node]
                continue

            new_distance = weight + distance[node]

            if new_distance < distance[destination]:
                distance[destination] = new_distance
                parent[destination] = node
                updated = True

        if not updated:
            break

    return distance, parent


def find_edges(edges):
    graph = {}
    edges = []
    for el in range(edges_count):
        source, destination, weight = [int(x) for x in input().split()]
        edges.append((source, destination, weight))

    return edges


nodes = int(input())
edges_count = int(input())

edges = find_edges(edges_count)

start = int(input())
target = int(input())

distance, parent = find_destinations()

if find_negative_cycle():
    print(f"Negative Cycle Detected")

else:
    print(find_path(distance[target]))
