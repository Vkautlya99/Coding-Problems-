# Last Non repeating Vharacter in a string 

def LastNonRepeatingCharacterInAnString(string):
    char_count = {}
    
    for char in string :
        char_count[char] = char_count.get(char, 0) + 1
        
    for char in reversed(string) :
        if char_count[char] == 1:
            return char 
    return None 

string = "vikramkumar"
print(LastNonRepeatingCharacterInAnString(string))    #u
           



