
nums = [int(x) for x in input().split()]

is_sorted = False
filled_cells = 0

while not is_sorted:
    is_sorted = True
    for idx in range(1, len(nums) - filled_cells):
        if nums[idx] < nums[idx - 1]:
            nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
            is_sorted = False

    filled_cells += 1

print(' '.join(str(x) for x in nums))

# tova e po dobriqt variqnt zaradi bulevata promenliva, koqto shte prekrati vednaga shtom chislata sa sortirani !