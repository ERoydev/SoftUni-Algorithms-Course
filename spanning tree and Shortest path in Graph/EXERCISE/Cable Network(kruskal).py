from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]

    return node


budget = int(input())
nodes = int(input())
edges = int(input())

forest = set()
graph = []
parent = [num for num in range(nodes)]
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    edge_data = input().split()
    first, second, weight = int(edge_data[0]), int(edge_data[1]), int(edge_data[2])
    graph[first].append(Edge(first, second, weight))
    graph[second].append(Edge(second, first, weight))

    if len(edge_data) == 4:
        ROOT = first
        forest.add(first)
        forest.add(second)

pq = PriorityQueue()
used_budget = 0
for node in forest:
    parent[node] = ROOT

    for edge in graph[node]:
        pq.put(edge)


while not pq.empty():
    edge = pq.get()
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)

    if first_node_root != second_node_root and used_budget + edge.weight < budget:
        parent[first_node_root] = second_node_root
        used_budget += edge.weight

        for edge in graph[edge.second]:
            pq.put(edge)


print(f"Budget used: {used_budget}")
