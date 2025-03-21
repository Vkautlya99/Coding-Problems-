
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


def TwoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
               return [i, j]
    return "No two sum solution"

target = 21
arr = [2, 7, 11, 15]
print(TwoSum(arr, target))


# METHOD : 2 - Using Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)

def TwoSumUsingHashMap(array, targetnum):
    num_map = {}
    
    for i, num in enumerate(array):
        compliment = targetnum - num 
        if compliment in num_map :
            return [num_map[compliment], num]
        num_map[num] = num
    return "No two sum solution"

array = [2, 7, 11, 15]
targetnum = 22
print(TwoSumUsingHashMap(array, targetnum))




