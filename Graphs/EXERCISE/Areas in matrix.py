def dfs(row, col, matrix, visited, parent):
    if 0 > row or row > rows-1 or 0 > col or col > cols-1:
        return

    if visited[row][col]:
        return

    if matrix[row][col] != parent:
        return

    visited[row][col] = True
    dfs(row, col + 1, matrix, visited, parent)
    dfs(row, col - 1, matrix, visited, parent)
    dfs(row-1, col, matrix, visited, parent)
    dfs(row+1, col, matrix, visited, parent)


rows = int(input())
cols = int(input())
matrix = []
visited = []
areas = {}

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue

        key = matrix[row][col]
        dfs(row, col, matrix, visited, key)

        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1

print(f"Areas: {sum(areas.values())}")

for key, value in sorted(areas.items()):
    print(f"Letter '{key}' -> {value}")
