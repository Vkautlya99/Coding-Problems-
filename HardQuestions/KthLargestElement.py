# Kth largest Element Using HeapQ
import heapq
def KthLargest(arr, k):
    return heapq.nlargest(k, arr)[-1]
    
arr = [1, 2, 3, 4, 5, 6, 9, 10, 8]
k = 3
print(KthLargest(arr, k))   #8

# Kth largest Element Using QuickSelect

import random

def quickselect(arr, k, low, high):
    if low <= high:
        pivot_index = partition(arr, low, high)
        
        if pivot_index == len(arr) - k:
            return arr[pivot_index]
        elif pivot_index > len(arr) - k:
            return quickselect(arr, k, low, pivot_index - 1)
        else:
            return quickselect(arr, k, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def kth_largest_quickselect(arr, k):
    arr_copy = arr[:]  # Create a copy to avoid modifying the original array
    return quickselect(arr_copy, k, 0, len(arr_copy) - 1)

# Example
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"{k}th largest element: {kth_largest_quickselect(arr, k)}")


