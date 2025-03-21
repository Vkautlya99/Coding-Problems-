def RemoveDuplicateFromUnsortedArray(array):
    set_arr = set()
    res = []
    for num in array :
        if num not in set_arr:
            set_arr.add(num)
            res.append(num)
    return res

array = [2,5,1,4,7,3,5,6,7,12,3]
print(RemoveDuplicateFromUnsortedArray(array))



#METHOD : 2 (if res array need to be in sorted format)

def sol(arr):
    set_seen = set(arr)
    return list(set_seen)

arr = [6,5,6,4,3,4,3,1,2,2]
print(sol(arr))

