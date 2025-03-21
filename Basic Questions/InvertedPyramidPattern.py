
def InvertedEquilateralTriangle(row):
    for i in range(row, -1, -1):
        print(" " * (row - i) + "*" * (2 * i - 1))

row = 6
InvertedEquilateralTriangle(row)



