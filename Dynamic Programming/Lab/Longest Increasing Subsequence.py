from collections import deque

sequence = [int(x) for x in input().split()]
length = [int(0) for _ in range(len(sequence))]
parent = [None] * (len(sequence))

length[0] = 1
parent[0] = -1

lis = [sequence[0]]
idx = 1

while True:
    if idx == len(sequence):
        break

    if not lis:
        lis.append(sequence[idx])
        parent[idx] = -1
        length[idx] = len(lis)
        idx += 1
        continue

    if sequence[idx] > lis[-1]:
        lis.append(sequence[idx])
        length[idx] = len(lis)
        parent[idx] = sequence.index(lis[-2])
        idx += 1

    else:
        if sequence[idx] > sequence[idx - 1]:
            lis.pop(-1)

path = deque()
element = length.index(max(length))

while element >= 0:
    path.appendleft(sequence[element])
    element = parent[element]

print(*path, sep=' ')