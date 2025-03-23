#Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.


def AlternateNumbers(arr):
    positive = []
    negative = []
    
    for num in arr :
        if num >= 0 :
            positive.append(num)
        else :
            negative.append(num)
    i, j = 0,0
    res = []
    
    while i < len(positive) and j < len(negative):
        res.append(positive[i])
        res.append(negative[j])
        i += 1
        j += 1
    while i <len(positive):
        res.append(positive[i])
        i += 1
    while j < len(negative):
        res.append(negative[j])     
        j += 1
    return res

arr = [-2, 3, -4, -1,5,6,-2,1]
print(AlternateNumbers(arr))   
arr = [-2, 3, -4, 5]
print(AlternateNumbers(arr))  # [3, -2, 5, -4]
            


