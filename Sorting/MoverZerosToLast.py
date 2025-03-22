def MoveZerosToLast(arr):
    positive_num = 0
    
    for num in range(len(arr)):
        if arr[num] != 0 :
            arr[num] , arr[positive_num] = arr[positive_num] , arr[num]
            positive_num += 1
    return arr

arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]     #TC: O(n) SC: O(1)
print(MoveZerosToLast(arr))                        