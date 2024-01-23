def two_sum_all_pair(nums, k):
    left = 0
    right = len(nums) - 1
    result = []
    
    while left <= right:
        if nums[left] + nums[right] < k:
            left += 1
        elif nums[left] + nums[right] > k:
            right -= 1
        else:
            result.append([left, right])
            left += 1
            right -= 1

    return result

nums = [-1, 1, 5, 7]
k = 6
print(two_sum_all_pair(nums, k))
