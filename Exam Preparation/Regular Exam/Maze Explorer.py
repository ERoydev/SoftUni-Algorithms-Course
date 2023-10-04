def find_path(row, col, matrix, path):
    if row >= len(matrix) or row < 0 or col >= len(matrix[0]) or col < 0:
        return

    if matrix[row][col] == "E":
        final.append([int(x) for x in path])
        return

    if matrix[row][col] == "#":
        return

    if matrix[row][col] == "v":
        return

    matrix[row][col] = "v"
    path.append(1)

    find_path(row, col + 1, matrix, path)
    find_path(row, col - 1, matrix, path)
    find_path(row - 1, col, matrix, path)
    find_path(row + 1, col, matrix, path)
    matrix[row][col] = "."

    path.pop(0)


size = int(input())
path = []
matrix = []
final = []

for row in range(size):
    matrix.append(list(input()))


find_path(0, 0, matrix, path)

element = min(len(x) for x in final)
print(element)
