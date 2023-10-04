
#drugiqt nachin e posredstvom matrica
nums = [int(x) for x in input().split()]

for i in range(len(nums)): #tova zamestva While loopa
    for j in range(1, len(nums) - i): #a tova realno e bubble sort actiona
        if nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]


print(*nums, sep=" ")

# tova e po loshiq variant osven, ako ne sloja buleva promenliva za da detectne koga ne sum promenql lista