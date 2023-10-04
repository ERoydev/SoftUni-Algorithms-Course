
def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]

    return node


nodes = int(input())
edges_count = int(input())

graph = []

for _ in range(edges_count):
    source, destination, weight = [int(x) for x in input().split(" - ")]
    graph.append((source, destination, weight))

parent = [num for num in range(nodes)]
forest = 0

for first, second, weight in sorted(graph, key=lambda x: x[2]):
    first_node_root = find_root(parent, first)
    second_node_root = find_root(parent, second)

    if first_node_root != second_node_root:
        parent[first_node_root] = second_node_root
        forest += weight

print(f"Total cost: {forest}")

