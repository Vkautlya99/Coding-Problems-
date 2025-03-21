def rightAngleTriangle(row):
    for i in range(1, row + 1):
        print("" * (row - i) + "* " * (2 * i - 1))
    
        
row = 5
rightAngleTriangle(row)

