def merge_arrays(left, right):
    result = [None] * (len(left) + len(right))
    left_idx = 0
    right_idx = 0
    result = []

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1

        else:
            result.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1

    return result


def mergesort(nums):
    if len(nums) == 1:
        return nums

    mid_idx = len(nums) // 2
    left = nums[0:mid_idx]
    right = nums[mid_idx::]

    return merge_arrays(mergesort(left), mergesort(right))


nums = [int(x) for x in input().split()]
result = mergesort(nums)
print(*result, sep=" ")