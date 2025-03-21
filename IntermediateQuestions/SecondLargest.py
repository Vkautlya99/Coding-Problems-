def SecondLargestElementInArray(arr):
    min_elem = float('-inf')
    largest = min_elem
    
    for num in arr:
        if num > largest:
            largest = num
    second_largest = min_elem
    for num in arr:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest

arr = [7,2,3,4,9,6]

print(SecondLargestElementInArray(arr))
    
#Optimized source code
#Time Complexity : O(n)
def second_largest_single_traversal(arr):
    if len(arr) < 2:
        return "No second largest element"

    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest  # Pehle largest ko second_largest banao
            largest = num  # Phir largest update karo
        elif num > second_largest and num < largest:
            second_largest = num  # Agar num unique aur second largest hai toh update karo

    return second_largest 

arr = [7, 2, 3, 4, 9, 6]
print(second_largest_single_traversal(arr))  # Output: 7
  
    
    