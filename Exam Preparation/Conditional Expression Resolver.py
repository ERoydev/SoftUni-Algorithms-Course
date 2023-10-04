
#t?t?4:2:1

def solver(line, idx):
    if line[idx].isdigit():
        return line[idx]

    if line[idx] == 't':
        return solver(line, idx + 2)

    cursor = idx + 2
    conditional_statements_counter = 0

    while True:
        symbol = line[cursor]
        if symbol == "?":
            conditional_statements_counter += 1

        elif symbol == ':':
            if conditional_statements_counter == 0:
                return solver(line, cursor + 1)
            conditional_statements_counter -= 1

        cursor += 1


expression = input().split()
print(solver(expression, 0))