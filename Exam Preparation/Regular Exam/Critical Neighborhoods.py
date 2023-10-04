from queue import PriorityQueue
from collections import deque

class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


edges = int(input())

graph = {}

for _ in range(edges):
    first, second, weight = [int(x) if x.isdigit() else str(x) for x in input().split(" - ")]
    edge = Edge(first, second, weight)
    graph[first] = graph.get(first, [])
    graph[second] = graph.get(second, [])

    graph[first].append(edge)
    graph[second].append(edge)


closed_roads = [x.split("-") for x in input().split(",")]


start_node = input()
end_node = input()

distance = {}
parent = {}

for key in graph.keys():
    distance[key] = float('inf')
    parent[key] = None

distance[start_node] = 0

pq = PriorityQueue()
pq.put((0, start_node))

while not pq.empty():
    min_distance, node = pq.get()
    if node == end_node:
        break

    for edge in graph[node]:
        founded = False
        for element in closed_roads:
            if (edge.first == element[0] or edge.first == element[1]) and (edge.second == element[0] or edge.second == element[1]):
                founded = True
                break

        if founded:
            continue

        new_distance = min_distance + edge.weight

        if edge.first == node and new_distance < distance[edge.second]:
            distance[edge.second] = new_distance
            parent[edge.second] = node
            pq.put((new_distance, edge.second))

        elif edge.second == node and new_distance < distance[edge.first]:
            distance[edge.first] = new_distance
            parent[edge.first] = node
            pq.put((new_distance, edge.first))


path = deque()
node = end_node

while node is not None:
    path.appendleft(node)
    node = parent[node]

print(*path, sep=' - ')

print(distance[end_node])

