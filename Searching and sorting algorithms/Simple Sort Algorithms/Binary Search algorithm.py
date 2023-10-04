
#Iterativen podhod ----> Po dobur ot dvata
def binary_search(collection, target):
    left = 0
    right = len(collection) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_element = collection[mid_idx]

        if target == mid_element:
            return mid_idx

        if target > mid_element:
            left = mid_idx + 1

        else:
            right = mid_idx - 1

    return -1


nums = [int(x) for x in input().split()]
target = int(input())

print(binary_search(nums, target))

#-----------------------------------------------------------------------------------------------#

#Recursion podhod
def binary_search(collection, target, left, right):

    mid_idx = (left + right) // 2
    mid_el = collection[mid_idx]

    if mid_el == target:
        return mid_idx

    if left == right:
        return f"Nqma takova chislo"

    if mid_el < target:
        left = mid_idx + 1

    else:
        right = mid_idx - 1

    return binary_search(collection, target, left, right)


nums = [int(x) for x in input().split()]
target = int(input())

print(binary_search(nums, target, 0, len(nums) - 1))