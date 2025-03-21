
#Dutch National flag or sort the 0s, 1s and 2s in an array 

def SortTheZerosOnesandTwos(arr):
    arr.sort()
    
arr = [0, 1, 2, 0, 1, 2]
# print(SortTheZerosOnesandTwos(arr))
print(arr)

#Optimized source code 

def sol(array):
    count_zero , count_one, count_two = 0,0,0
    
    for num in array :
        if num == 0 :
            count_zero += 1
        elif num == 1:
            count_one += 1
        else:
            count_two += 1
    array[:count_zero] = [0] * count_zero
    array[count_zero:count_zero + count_one] = [1] * count_one
    array[count_zero + count_one:] = [2] * count_two

array = [0, 1, 2, 0, 1, 2]

print(array)




