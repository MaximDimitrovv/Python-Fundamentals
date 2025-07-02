nums = list(map(int, input().split()))
total_sum = 0

while len(nums) > 0:
    index = int(input())

    if index < 0:
        removed = nums[0]
        nums[0] = nums[-1]  # копира последния елемент на мястото на първия
    elif index >= len(nums):
        removed = nums[-1]
        nums[-1] = nums[0]  # копира първия елемент на мястото на последния
    else:
        removed = nums.pop(index)

    total_sum += removed

    for i in range(len(nums)):
        if nums[i] <= removed:
            nums[i] += removed
        else:
            nums[i] -= removed

print(total_sum)