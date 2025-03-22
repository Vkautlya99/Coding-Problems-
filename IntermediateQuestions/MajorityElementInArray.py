# Given an array arr. Find the majority element in the array. If no majority exists, return -1.
# A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.

def MajorityElement(arr):
    count = 0
    candidate = None
    
    for num in arr :
        if count == 0 :
            candidate = num 
            count = 1
            
        elif num == candidate :
            count += 1
        else :
            count -= 1
    freq = 0 
    for num in arr :
        if num == candidate:
            freq += 1
    if freq > len(arr)//2 :
        return candidate 
    else :       
        return -1

arr = [1, 2, 3, 4, 5, 6, 8, 9, 10, 8, 8, 8,8,8,8,8,8,8,8]
print(MajorityElement(arr)) 


#METHOD 2 
def sol(array):
    n = len(array)
    return array[n//2]

array = [1, 2, 3, 4, 5, 6, 8, 9, 10, 8, 8, 8,8,8,8,8,8,8,8]
print(sol(array))  #8


