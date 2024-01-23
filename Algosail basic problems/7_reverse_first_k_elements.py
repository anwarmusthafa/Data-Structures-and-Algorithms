def reverse_first_k_elements(nums,k):
    left = 0
    right = k-1
    while left <= right:
        nums[left] , nums[right] = nums[right], nums[left]
        right -= 1
        left += 1
    return nums
nums = [1,2,3,4,5,6,7]
k = 3
print(reverse_first_k_elements(nums,k))