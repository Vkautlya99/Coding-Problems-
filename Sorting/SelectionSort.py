def Selection_Sort(arr):
    for i in range(len(arr) - 1):
        min_elem = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_elem]:
                min_elem = j
        arr[i], arr[min_elem] = arr[min_elem], arr[i]
    return arr

arr = [3,1,5,6,2,0]
print(Selection_Sort(arr))    
    
    
    
    