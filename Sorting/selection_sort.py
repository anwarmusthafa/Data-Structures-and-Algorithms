def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_pos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[min_pos]:
                min_pos = j
        
        nums[i],nums[min_pos] = nums[min_pos], nums[i]
    return nums

nums = [4,3,2,5,6,44,55,33,4,55,67,47]
print(selection_sort(nums))