# Kth Largest Element in an Using sorting (Tim Sort)

def KthLargest(arr, k):
    arr.sort()
    return arr[-k]

arr = [1, 2, 3, 4, 5, 6, 9, 10, 8]
k = 2
print(KthLargest(arr, k))   #8

