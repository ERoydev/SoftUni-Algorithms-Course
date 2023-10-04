"""
Na BFS za vseki node dobavqm nego i negovite child v moqta opashka i visited
i posle za vseki node v opashakta dobavqm i negovite childs i taka
po opashkata gi izkarvam edin po edin na vsqka iteraciq
"""

from collections import deque

graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    1: [7],
    12: [],
    31: [21],
    21: [14],
    14: [23, 6],
    6: [],
    23: [21]
}

visited = set()


def bfs(node, graph, visited):
    if node in visited:
        return

    queue = deque([node])
    visited.add(node)

    while queue:
        current_node = queue.popleft()
        print(current_node)

        for child in graph[current_node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)


for node in graph:
    bfs(node, graph, visited)


