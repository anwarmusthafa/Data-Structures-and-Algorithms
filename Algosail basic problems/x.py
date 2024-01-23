def removeDuplicates(nums):
        left = 0
        right = 1
        while right <= len(nums) - 1:
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
        return nums

print(removeDuplicates([1,1,2]))