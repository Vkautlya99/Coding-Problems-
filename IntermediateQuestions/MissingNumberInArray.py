def MissingNumberInAnArray(arr):
    n = len(arr) + 1
    expected_sum = (n * (n + 1)) // 2
    
    actual_sum = sum(arr)
    
    missing_elem = expected_sum - actual_sum
    return missing_elem

arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]
print(MissingNumberInAnArray(arr))