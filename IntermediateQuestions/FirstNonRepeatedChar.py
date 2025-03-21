def FirstNonRepeatedCharacterInAString(string):
    count = {}
    
    for char in string:
        if char not in count :
            count[char] = 1
        else :
            count[char] += 1
    for char in count :
        if count[char] == 1:
            return char
        
string = "vikrammav"
print(FirstNonRepeatedCharacterInAString(string))