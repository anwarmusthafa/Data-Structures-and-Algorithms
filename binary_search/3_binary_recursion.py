def binary_search_recursion(nums,num,left,right):
    if right < left:
        return "Number not found"
    mid = (left+right) // 2
    mid_value = nums[mid]
    if mid_value == num:
        return f"Number founf at {mid} index"
    if mid_value < num:
        left = mid+1
    else:
        right = mid - 1
    
    return binary_search_recursion(nums,num,left,right)

nums = [1,3,5,6,12,13,45,56,67,89]
num = 13
print(binary_search_recursion(nums,num,0,len(nums) - 1))