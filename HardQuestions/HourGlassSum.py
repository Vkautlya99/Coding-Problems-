def find_max_hourglass_sum(matrix):
    # Ensure matrix has at least 3x3 dimensions to contain an hourglass
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows < 3 or cols < 3:
        raise ValueError("Matrix must be at least 3x3 to contain an hourglass.")
    
    # Initialize maximum sum to a very small number
    max_sum = float('-inf')
    
    # Traverse each potential hourglass top-left corner
    for i in range(rows - 2):
        for j in range(cols - 2):
            # Calculate the sum of the current hourglass
            current_sum = (
                matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] +  # top row
                matrix[i + 1][j + 1] +                              # middle element
                matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]  # bottom row
            )
            
            # Update max_sum if the current_sum is greater
            max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
matrix = [
    [1, 2, 3, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 2, 4, 4],
    [0, 0, 0, 2, 0]
]

result = find_max_hourglass_sum(matrix)                  # TC :- O(n * m)
print("Maximum hourglass sum:", result)                  # SC :- O(1)