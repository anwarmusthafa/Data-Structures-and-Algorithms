
def binary_search(number_list, number_to_find):
    left = 0
    right = len(number_list) - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if number_list[mid] == number_to_find:
            return mid
        if number_to_find < number_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return "Number not found"
number_list = [1,2,3,4,5,6,7,8,9]
number_to_find = 3
result = binary_search(number_list,number_to_find)
if isinstance(result, str):
    print("Not found")
else:
    print(result + 1)
    
