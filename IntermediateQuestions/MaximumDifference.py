def MaximumDifferenceInAnArray(Array):
    max_elem = float("-inf")
    min_elem = float("inf")
    
    for num in Array:
        if num > max_elem:
            max_elem = num 
        if num < min_elem:
            min_elem = num 
        diff = max_elem - min_elem
    return diff 

Array = [2,4,1,6,8,9]
print(MaximumDifferenceInAnArray(Array))