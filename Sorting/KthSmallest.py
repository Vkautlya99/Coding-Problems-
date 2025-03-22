# Kth Smallest using sorting 


def KthSmallestUsingSorting(arr, k):
    arr.sort()
    return arr[k-1]

arr = [8,9,6,5,4,2,7]
k = 3   
print(KthSmallestUsingSorting(arr, k))   #4

