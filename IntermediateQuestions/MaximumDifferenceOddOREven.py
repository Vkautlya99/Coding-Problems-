def MaximumDifferenceIsOddorEven(arr):
    min_elem = float("inf")
    max_elem = float("-inf")
    
    for num in arr :
        if num < min_elem :
            min_elem = num 
        if num > max_elem :
            max_elem = num 
        diff = max_elem - min_elem
    if diff % 2 == 0 :
        return "EVEN"
    else :
        return "ODD"

arr = [2,5,1,3,7,10]
print(MaximumDifferenceIsOddorEven(arr))


