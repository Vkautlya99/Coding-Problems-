
def LeapYear(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    else :
        return False

year = 2003
print(LeapYear(year))


# Second Type Question 

def StartAndEndLeap(start, end):
    for year in range(start, end):
        if (year % 4 == 0 and year % 400 != 0) or (year % 100 == 0):
            print(year)

start = 1998
end = 2003
StartAndEndLeap(start, end)

