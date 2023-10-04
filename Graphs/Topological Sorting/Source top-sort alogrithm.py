def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0

        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1

    return result


def find_node_without_dependencies(dependencies_by_node): #detect cycle in graph
    for item in dependencies_by_node:
        if dependencies_by_node[item] == 0:
            return item

    return None


n = int(input())
graph = {
}

for idx in range(n):
    line = input().split("->")
    node = line[0].strip()
    children = line[1].strip().split(", ") if line[1] else []

    graph[node] = children

dependencies_by_node = find_dependencies(graph)

has_cycles = False
sorted_nodes = []

while dependencies_by_node:
    node_to_remove = find_node_without_dependencies(dependencies_by_node)
    if node_to_remove is None:
        has_cycles = True
        break

    sorted_nodes.append(node_to_remove)
    dependencies_by_node.pop(node_to_remove)

    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

if has_cycles:
    print(f"Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(str(x) for x in sorted_nodes)}")