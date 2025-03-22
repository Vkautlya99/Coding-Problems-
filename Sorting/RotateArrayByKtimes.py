# Left Rotate array by D places


def RotateElement(arr, d):
    n = len(arr)
    d = d % n

    arr[:] = arr[d:] + arr[:d]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
print(RotateElement(arr, d))  #[3, 4, 5, 6, 7, 1, 2]


#METHOD 2 by reversal algorithm

def reverse(arr, start, end):
    while start < end :
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    
def rotate(arr, d):
    n = len(arr)
    d = d % n
    
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)
    
    return arr


arr = [1,2,3,4,5,6,7,8,9,10]
d = 3
print(rotate(arr, d))  #[4, 5, 6, 7, 99, 10, 1, 2, 3]
    
    




