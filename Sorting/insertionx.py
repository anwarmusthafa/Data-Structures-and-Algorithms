# def insertion_sort(nums):
#     for i in range(1,len(nums)):
#         key = nums[i]
#         j = i -1
#         while j >= 0 and key < nums[j]:
#             nums[j+1] = nums[j]
#             j -= 1
#         nums[j+1] = key
#     return nums

def insertion_sort(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i - 1
        while j > 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = key
    return nums
nums = [2,3,1,2,3,5,43,45,21,132,4]
print(insertion_sort(nums))
