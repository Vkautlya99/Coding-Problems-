def Bubble_Sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i] :
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [4,0,2,3,1,5]
print(Bubble_Sort(arr))


