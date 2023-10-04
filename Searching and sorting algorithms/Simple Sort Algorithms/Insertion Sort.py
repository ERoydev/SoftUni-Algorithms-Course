nums = [int(x) for x in input().split()]

for j in range(1, len(nums)):
    for i in range(j, 0, -1):
        if nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]

        else:
            break

print(*nums, sep=' ')


# drugiq variqnt

for i in range(len(nums)):
    j = i
    while j > 0 and nums[j] < nums[j - 1]:
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
        j -= 1


