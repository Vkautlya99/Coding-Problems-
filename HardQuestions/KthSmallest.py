# Kth Smallest Element in an array Using heapq
import heapq
def KthSmallestElement(arr, k):
    return heapq.nsmallest(k, arr)[-1]

arr = [8,9,6,5,4,2,7]
k = 3
print(KthSmallestElement(arr, k))   #3    


