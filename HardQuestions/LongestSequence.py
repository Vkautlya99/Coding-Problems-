# #Longest Consecutive Subsequence
# Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.


def LongestSubsequence(arr):
    if len(arr) < 2 :
        return 0
    
    num_set = set(arr)
    max_length = 0
    
    for num in arr :
        if num - 1 not in num_set:
            curr_num = num
            curr_length = 1
            
            while curr_num + 1 in num_set :
                curr_num += 1
                curr_length += 1
                
            max_length = max(max_length, curr_length)
    return max_length

arr = [1, 9, 3, 10, 4, 20, 2]
print(LongestSubsequence(arr)) #4
arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
print(LongestSubsequence(arr)) #5

