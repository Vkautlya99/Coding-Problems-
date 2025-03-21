def FibbonacciNumber(num):
    if num < 0 :
        return False
    
    a , b = 0, 1
    while a <= num :
        if a == num :
            return True
        a, b = b , b + a
    return False 

num = 35
print(FibbonacciNumber(num))
        