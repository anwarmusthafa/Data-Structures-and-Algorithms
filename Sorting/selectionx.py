# def selection_sort(nums):
#         for i in range(len(nums)):
#             min_pos = i
#             for j in range(i,len(nums)):
#                 if nums[j] < nums[min_pos]:
#                     min_pos = j
#             nums[i],nums[min_pos] = nums[min_pos],nums[i]
#         return nums

def selection_sort(nums):
    for i in range(len(nums)):
        min = i
        for j in range(i,len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i],nums[min] = nums[min],nums[i]
    return nums

nums = [5,9,4,6,3,22,3,44,33,5,4,0,1,-1]
print(selection_sort(nums))