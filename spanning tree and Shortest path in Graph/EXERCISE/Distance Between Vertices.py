from collections import deque


def find_parent_by_node(graph, source, destination):
    queue = deque([source])
    visited = {source}

    parent = {source: None}

    while queue:
        node = queue.popleft()

        if node == destination:
            break

        for child in graph[node]:
            if child in visited:
                continue

            visited.add(child)
            queue.append(child)
            parent[child] = node

    return parent


def find_steps(parent, destination):
    steps = 0
    node = destination
    while node is not None:
        steps += 1
        node = parent[node]

    return steps - 1


nodes = int(input())
pairs = int(input())

graph = {}

for _ in range(nodes):
    node_str, children_str = input().split(":")
    children = [int(x) for x in children_str.split()] if children_str else []
    node = int(node_str)

    graph[node] = children


for _ in range(pairs):
    source, destination = [int(x) for x in input().split("-")]

    parent = find_parent_by_node(graph, source, destination)

    if destination not in parent:
        print(f"{{{source}, {destination}}} -> -1")
        continue

    count_steps = find_steps(parent, destination)

    print(f"{{{source}, {destination}}} -> {count_steps}")





