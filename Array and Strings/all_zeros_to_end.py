a = [0,1,0,3,12]
def move_zeros_to_end(arr):
    count = 0  # Count of non-zero elements
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] =arr[i]
            count += 1
    while count<len(arr):
        arr[count]= 0
        count+=1
    return arr

print(f'All zeroes moved to end: {move_zeros_to_end(a)}')
