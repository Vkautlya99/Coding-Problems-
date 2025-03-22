# Find the Nearest Prime number 


def is_Prime(num):
    if num < 2:
        return False
    # for i in range(2, int(num ** 0.5) + 1):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def NearestPrimeNumber(n):
    for num in range(n - 1, 1 , -1):
        if is_Prime(num):
            return num
    return None 
        
n = 20
print(NearestPrimeNumber(n))  #11
    


