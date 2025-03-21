def ArrayReverse(array):

    rev_arr = []
    for num in range(len(array) - 1, -1, -1) :
        rev_arr.append(array[num])
    return rev_arr

array = [1,2,3,4,5,6,7,8,9]
print(ArrayReverse(array))


