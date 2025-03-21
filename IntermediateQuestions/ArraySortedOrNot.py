def ArrayisSortedOrNot(arr):
    for i in range(1,len(arr)):
        if arr[i - 1] > arr[i]:
            return "Array is Not Sorted"
    return "Array is Sorted"

array1 = [1, 2, 3, 4, 5, 6]
print(ArrayisSortedOrNot(array1))


array2 = [1, 2, 3, 4, 5, 6, 3]
print(ArrayisSortedOrNot(array2))