#Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.


def MaximumProductSubArray(arr):
    curr_max = arr[0]
    curr_min = arr[0]
    max_product = arr[0]
    
    for num in arr :
        if num < 0 :
            curr_max, curr_min = curr_min, curr_max
        curr_max = max(num , curr_max * num)
        curr_min = min(num , curr_min * num)
        max_product = max(max_product, curr_max)
    return max_product

arr = [2,3,-2,4]
print(MaximumProductSubArray(arr)) # 6   


