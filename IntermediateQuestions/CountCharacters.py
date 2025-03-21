def CountCharactersOfAString(string):
    count = {}
    for char in string :
        if char not in count :
            count[char] = 1
        else :
            count[char] += 1
            
    return count

string = "viikrkam"
print(CountCharactersOfAString(string))