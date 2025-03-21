def SecondSmallestInAnArray(arr):
    smallest = float('inf')
    second_smallest = float('inf')
    
    for num in arr :
        if num < smallest :
            second_smallest = smallest 
            smallest = num 
        elif num < second_smallest and num != smallest :
            second_smallest = num
    return second_smallest

arr= [7,1,9,8]
print(SecondSmallestInAnArray(arr))