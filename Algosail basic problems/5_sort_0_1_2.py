#dutch national flag
def sort_0_1_2(arr):
    low = 0
    i = 0
    high = len(arr) - 1
    while i <= high:
        if arr[i] == 0:
            arr[i],arr[low] = arr[low],arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i],arr[high] = arr[high],arr[i]
            high -= 1
    return arr

arr = [1,2,1,0,0,2,1,0,1,1,0]
print(sort_0_1_2(arr))
        
