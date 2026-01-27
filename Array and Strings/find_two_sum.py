# def two_sum(arr,goal):
#     count = []
#     for i in range(len(arr)-1):

#         for j in range(i+1,len(arr)):
        
#           if arr[i]+arr[j] == goal:
#                     count.append((i,j)) 

#     return count

# print(two_sum([1,2,3,4,5],5))
def two_sum_fast(arr, goal):
    seen = {} # value : index
    results = []
    for i, num in enumerate(arr):
        diff = goal - num
        if diff in seen:
            results.append((seen[diff], i))
        seen[num] = i
    return results
print(two_sum_fast([1,2,3,4,5],5))