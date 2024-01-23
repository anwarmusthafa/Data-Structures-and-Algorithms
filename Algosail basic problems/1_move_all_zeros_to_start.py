def move_zero_to_start(nums):
    n = len(nums)
    zero_index = n-1
    for i in range(n-1,-1,-1):
        if nums[i] != 0:
            nums[i],nums[zero_index] = nums[zero_index],nums[i]
            zero_index -= 1
    return nums

    
print(move_zero_to_start([5,6,0,1,0]))

#anotther approach
    # low = 0
    # for i in range(len(nums)):
    #     if nums[i] == 0:
    #         nums[i],nums[low] = nums[low], nums[i]
    #         low += 1
    # return nums



