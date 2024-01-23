def move_zeros_end(nums):
    high = len(nums) - 1
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == 0:
            nums[i], nums[high] = nums[high], nums[i]
            high -= 1
    return nums

print(move_zeros_end([0,0,1]))
                