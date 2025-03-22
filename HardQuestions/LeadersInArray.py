#Leaders in an array

def LeaderInAnArray(arr):
    leader = 0
    res = []
    
    for i in range(len(arr) - 1, -1 , -1 ):
        if arr[i] > leader :
            leader = arr[i]
            res.insert(0, leader)
    return res

arr = [16, 17, 4, 3, 5, 2]
print(LeaderInAnArray(arr))  #[17, 5, 2]


