from collections import deque


def check(row, col):
    if row < 0 or col < 0:
        return 0

    return dp_matrix[row][col]


rows, cols = int(input()), int(input())
matrix, dp_matrix = [], []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp_matrix.append([0] * cols)

dp_matrix[0][0] = matrix[0][0]

for col in range(1, cols):
    dp_matrix[0][col] = dp_matrix[0][col - 1] + matrix[0][col]
    dp_matrix[col][0] = dp_matrix[col - 1][0] + matrix[col][0]

for row in range(1, rows):
    for col in range(1, cols):
        element = max(dp_matrix[row][col - 1], dp_matrix[row - 1][col])
        dp_matrix[row][col] = element + matrix[row][col]


row, col = rows - 1, cols - 1
path = deque([[row, col]])

while row > 0 or col > 0:
    n1 = check(row, col - 1)
    n2 = check(row - 1, col)

    if n1 >= n2:
        path.appendleft([row, col - 1])
        col -= 1

    else:
        path.appendleft([row - 1, col])
        row -= 1

print(*path, sep=" ")