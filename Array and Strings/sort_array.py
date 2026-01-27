def sort_array(arr):
    if len(arr)<= 1:
        return True
    for i in range(len(arr)-1):
        if arr[i]> arr[i+1]:
            return False
    return True

print(sort_array([3,6,7,8,9]))
print(sort_array([3,7,5,2,9]))