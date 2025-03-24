# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.


def DifferenceOfTwoArrays(arr1, arr2):
    res1 = []
    res2 = []
    for num in arr1 :
        if num not in arr2 :
            res1.append(num)
    for num in arr2 :
        if num not in arr1 :
            res2.append(num)
    return [res1, res2]

arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]
print(DifferenceOfTwoArrays(arr1, arr2)) #[[1, 2], [6, 7]]



# Time Complexity: O(n)
# Space Complexity: O(n)


#More efficient solution using set:

def DifferenceOfTwoArray(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    diff1 = list(set1 - set2)   
    diff2 = list(set2 - set1)
    
    return [diff1, diff2]

array1 = [1,2,3,4,5]
array2 = [3,4,5,6,7]
print(DifferenceOfTwoArray(array1, array2)) #[[1, 2], [6, 7]] 

# Time Complexity: O(n) 
# Space Complexity: O(n)


