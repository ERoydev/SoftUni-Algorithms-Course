
def reverse(idx, elements):
    swap_idx = len(array) - 1 - idx
    if idx >= len(elements) // 2:
        print(*elements, sep=" ")
        return

    elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
    reverse(idx + 1, elements)


array = [int(x) for x in input().split()]
counter = len(array)
swap = len(array) // 2

reverse(0, array)