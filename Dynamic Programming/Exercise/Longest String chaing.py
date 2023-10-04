from collections import deque

string = input().split()
seq = []

[seq.append(len(el)) for el in string]
length = [0] * len(string)
parent = [None] * len(string)

best_idx = 0
best_size = 1


for idx in range(len(seq)):
    current_number = seq[idx]
    current_best_size = 1
    current_parent = None

    for prev in range(idx - 1, -1 , -1):
        prev_number = seq[prev]

        if prev_number >= current_number:
            continue

        if length[prev] + 1 >= current_best_size:
            current_best_size = length[prev] + 1
            current_parent = prev

    length[idx] = current_best_size
    parent[idx] = current_parent

    if current_best_size > best_size:
        best_size = current_best_size
        best_idx = idx

path = deque()
while best_idx is not None:
    path.appendleft(string[best_idx])
    best_idx = parent[best_idx]

print(*path, sep=' ')