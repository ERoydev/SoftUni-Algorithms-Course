def dfs(node, graph, salaries):
    if salaries[node] is not None:
        return salaries[node]

    if len(graph[node]) == 0:
        salaries[node] = 1
        return 1

    salary = 0
    for child in graph[node]:
        salary += dfs(child, graph, salaries)

    salaries[node] = salary
    return salary

graph = []

employees = int(input())

for i in range(employees):
    line = input()
    graph.append([])
    for idx, state in enumerate(line):
        if state == "Y":
            graph[i].append(idx)


salaries = [None] * employees

result = 0
for node in range(len(graph)):
    salary = dfs(node, graph, salaries)
    result += salary

print(result)