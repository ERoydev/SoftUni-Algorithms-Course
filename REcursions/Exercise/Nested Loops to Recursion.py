def nested_loops(idx, n):
    if idx >= n:
        print(*vector)
        return

    for num in range(1, n+1):
        vector[idx] = num
        nested_loops(idx + 1, n)


n = int(input())
vector = [None] * n

nested_loops(0, n)