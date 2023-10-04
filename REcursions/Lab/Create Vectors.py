
def gen01(idx, vector):
    if idx >= n:
        print(''.join([str(x) for x in vector]))
        return

    for num in range(0, 2):
        vector[idx] = num
        gen01(idx + 1, vector)


n = int(input())
vector = [0] * n


gen01(0, vector)
