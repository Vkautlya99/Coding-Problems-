#Kadane's Algorithm
# Given an integer array arr[]. You need to find the maximum sum of a subarray.


def KadanesAlgorithm(arr):
    curr_sum = arr[0]
    max_sum = arr[0]
    
    for num in arr[1 :]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
        
    return max_sum

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(KadanesAlgorithm(arr))  #7
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]              #TC : O(n) SC : O(1)
print(KadanesAlgorithm(arr))  #6
    
    
    
    





