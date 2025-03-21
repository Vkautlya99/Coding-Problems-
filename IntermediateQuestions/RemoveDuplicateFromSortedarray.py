def RemoveDuplicateFromSortedArray(array):
    j = 0
    for i in range(1, len(array)):
        if array[i] != array[j]:
            j += 1
            array[j] = array[i]
    return array[:j + 1]


array = [1,2,3,3,4]
print(RemoveDuplicateFromSortedArray(array))
            

#METHOD : 2

def removeDuplicateFromSortedArray(arr):
    set_arr = set(arr)
    return list(set_arr)

arr = [1,2,3,3,4]
print(removeDuplicateFromSortedArray(arr))


    
    
    