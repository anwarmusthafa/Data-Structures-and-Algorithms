def hours_partition(nums):
    n = len(nums)
    left = 0
    right = n - 1
    
    while left < right:
        while left < n and nums[left] == 0:
            left += 1
        
        while right >= 0 and nums[right] == 1:
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums

array = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]
print(hours_partition(array))
