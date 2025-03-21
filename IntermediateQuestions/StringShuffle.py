# Checking valid shuffle of two Strings
# Given two strings str1 and str2, and a third-string shuffle, determine if shuffle is a valid shuffle of str1 and str2, where a valid shuffle contains all characters from str1 and str2 occurring the same number of times, regardless of order. Print “YES” if valid, and “NO” otherwise.

from collections import Counter;

def StringShuffle(s1, s2, shuffle):
    combined = s1 + s2 
    if Counter(combined) == Counter(shuffle):
        return "YES"
    return "NO"

print(StringShuffle("BA", "XY", "XYAB"))  # YES
print(StringShuffle("BA", "XY", "XUMB"))  # NO
print(StringShuffle("ABC", "ZYS", "YBAZSC"))  # YES
