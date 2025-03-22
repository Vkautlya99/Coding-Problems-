# Rotate an array by 1 place

def RotateArray(arr):
    arr[:] = arr[1:] +  arr[:1]
    return arr

arr = [1, 2, 3, 4, 5]
print(RotateArray(arr))  #[2, 3, 4, 5, 1]
    

#METHOD 2 :- By temp variable 

def RotateArrayByTempvariable(array):
    first_element = array[0]
    for i in range(len(array) - 1 ):
        array[i] = array[i+1]
    array[-1] = first_element
    return array

Array = [1, 2, 3, 4, 5]
print(RotateArrayByTempvariable(Array))  #[2, 3, 4, 5, 1]


