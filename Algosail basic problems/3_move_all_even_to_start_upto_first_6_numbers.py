def move_start(nums):
    n = 6
    even_index = n
    for i in range (n,-1,-1):
        if nums[i] % 2 != 0:
            nums[i],nums[even_index] = nums[even_index], nums[i]
            even_index -= 1
    return nums

list = [1,12,4,5,6,8,5,1,3,6,10]
print(move_start(list))