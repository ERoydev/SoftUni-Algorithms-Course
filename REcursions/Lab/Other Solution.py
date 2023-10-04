
def can_place_queen(row, col, rows, cols, left_diagonal, right_diagonal):
    if row in rows:
        return False

    if col in cols:
        return False

    if (row - col) in left_diagonal:
        return False

    if (row + col) in right_diagonal:
        return False

    return True


def set_queen(row, col, rows, cols, left_diagonal, right_diagonal):
    chessboard[row][col] = "*"
    rows.add(row)
    cols.add(col)
    left_diagonal.add(row - col)
    right_diagonal.add(row + col)


def remove_queen(row, col, rows, cols, left_diagonal, right_diagonal):
    chessboard[row][col] = "-"
    rows.remove(row)
    cols.remove(col)
    left_diagonal.remove(row - col)
    right_diagonal.remove(row + col)


def print_solution():
    for element in chessboard:
        print(*element)

    print()


def add_queen(row, col, rows, cols, left_diagonal, right_diagonal):
    if row == 8:
        print_solution()
        return

    for col in range(0, 8):
        if can_place_queen(row, col, rows, cols, left_diagonal, right_diagonal):
            set_queen(row, col, rows, cols, left_diagonal, right_diagonal)
            add_queen(row + 1, col, rows, cols, left_diagonal, right_diagonal)
            remove_queen(row, col, rows, cols, left_diagonal, right_diagonal)


chessboard = []
n = 8

[chessboard.append(["-"] * n) for _ in range(8)]

add_queen(0, 0, set(), set(), set(), set())