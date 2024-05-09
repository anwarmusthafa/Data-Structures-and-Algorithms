def insertion_sort(nums):
    for i in range(1,len(nums)):
        num = nums[i]
        j = i - 1
        while j >= 0 and num < nums[j]:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = num
    return nums

nums = [11,2,33,4,565,4,3]
print(insertion_sort(nums))
