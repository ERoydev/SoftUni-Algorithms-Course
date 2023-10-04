
def is_outside(row, col):
    return row < 0 or col < 0 or row >= len(chessboard) or col >= len(chessboard[0])


def check_diagonal(row, col):
    diagonal_sides = [[-1, -1], [-1, +1], [+1, -1], [+1, +1]]

    while diagonal_sides:
        current_side = diagonal_sides.pop(0)

        current_row, current_col = row, col

        while True:
            current_row += current_side[0]
            current_col += current_side[1]

            if is_outside(current_row, current_col):
                break

            if chessboard[current_row][current_col] == "*":
                return False

    return True


def check_horizont_vertical(row, queen_col):
    for idx in range(0, 8):
        if chessboard[row][idx] == "*" and idx != queen_col:
            return False

        if chessboard[idx][queen_col] == "*" and idx != row:
            return False

    return True


def can_place_queen(row, col):
    if check_horizont_vertical(row, col) and check_diagonal(row, col):
        return True


def set_queen(row, col):
    chessboard[row][col] = "*"


def remove_queen(row, col):
    chessboard[row][col] = "-"


def print_solution():
    for element in chessboard:
        print(*element)

    print()


def add_queen(row):
    if row == 8:
        print_solution()
        return

    for col in range(0, 8):
        if can_place_queen(row, col):
            set_queen(row, col)
            add_queen(row + 1)
            remove_queen(row, col)


chessboard = []
n = 8

[chessboard.append(["- "] * n) for _ in range(8)]

add_queen(0)