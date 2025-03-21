# Write a Code to check whether one string is a rotation of another in desi language


def StringIsRotatedOrNot(string1, string2):
    if len(string1) != len(string2):
        return False
    combined_str = string1 + string1
    if string2 in combined_str:
        return True
    return False

string1 = "ABCD"
string2 = "CDAB"
print(StringIsRotatedOrNot(string1, string2)) # True

string1 = "ABCD"
string2 = "ACBD"
print(StringIsRotatedOrNot(string1, string2)) # False
