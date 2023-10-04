def check_if_inside(row, col):
    return row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0])


def find_all_paths(row, col, destination, path):
    if check_if_inside(row, col):
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
        find_all_paths(row, col+1, "R", path)
        find_all_paths(row, col-1, "L", path)
        find_all_paths(row-1, col, "U", path)
        find_all_paths(row+1, col, "D", path)
        lab[row][col] = "-"

    path.pop()


lab = []

rows = int(input())
cols = int(input())

for i in range(rows):
    lab.append(list(input()))

find_all_paths(0, 0, "", [])

