from collections import deque

words = input().split()

size = [0] * len(words)
parent = [None] * len(words)
best_size = 0
best_idx = 1


for current in range(len(words)):
    current_number = len(words[current])
    current_size = 1
    current_parent = None

    for prev in range(current - 1, -1, -1):
        prev_number = len(words[prev])

        if prev_number >= current_number:
            continue

        if size[prev] + 1 >= current_size:
            current_size = size[prev] + 1
            current_parent = prev

    size[current] = current_size
    parent[current] = current_parent

    if current_size > best_size:
        best_size = current_size
        best_idx = current

path = deque()

while best_idx is not None:
    path.appendleft(words[best_idx])
    best_idx = parent[best_idx]

print(*path, sep=' ')


