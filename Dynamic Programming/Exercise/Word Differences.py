first = input()
second = input()

operations = 0
matrix = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

for row in range(1, len(first) + 1):
    matrix[0][row] = row
    matrix[row][0] = row

for row in range(1, len(first) + 1):
    for col in range(1, len(second) + 1):
        if first[row - 1] == second[col - 1]:
            matrix[row][col] = matrix[row -1][col - 1]
            continue

        matrix[row][col] = min(matrix[row - 1][col], matrix[row][col - 1]) + 1


print(f"Deletions and Insertions: {matrix[len(first)][len(second)]}")

#------------------------------

def find_operations(row, col, memo):
    key = f"{row} {col}"
    if key in memo:
        return memo[key]

    if row == 0 or col == 0:
        memo[key] = col if row == 0 else row
        return memo[key]

    if first[row - 1] == second[col - 1]:
        result = find_operations(row - 1, col - 1, memo)
        memo[key] = result

    else:
        result = min(find_operations(row - 1, col, memo), find_operations(row, col - 1, memo)) + 1
        memo[key] = result

    return result


first = input()
second = input()

operations = 0
matrix = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

print(f"Deletions and Insertions: {find_operations(len(first), len(second), {})}")