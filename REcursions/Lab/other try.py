def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row > rows-1 or col > cols-1


def find_paths(row, col, destination, lab, path):
    if is_outside(row, col, rows, cols):
        return

    if lab[row][col] == "*":
        return

    if lab[row][col] == "v":
        return

    path.append(destination)

    if lab[row][col] == "e":
        print(''.join(path))

    else:
        lab[row][col] = "v"
        find_paths(row, col + 1, "R", lab, path)
        find_paths(row, col - 1, "L", lab, path)
        find_paths(row - 1, col, "U", lab, path)
        find_paths(row + 1, col, "D", lab, path)
        lab[row][col] = "-"

    path.pop()


lab = []
rows = int(input())
cols = int(input())

for row in range(rows):
    lab.append(list(input()))


find_paths(0, 0, "", lab, [])