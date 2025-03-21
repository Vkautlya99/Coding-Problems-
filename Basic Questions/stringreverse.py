
def reverseTheString(s):
    # return s[::-1]
    rev = ""

    for char in s:
        rev = char + rev
    return rev
    
s = "12345"
print(reverseTheString(s))