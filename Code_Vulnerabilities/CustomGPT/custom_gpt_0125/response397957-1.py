
import numpy as np

# Example 2D array representing pixel values
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Function to calculate the distance based on the formula provided
def distance_function(pixel_value, row, col, center_row, center_col, L):
    d = np.sqrt((row - center_row) ** 2 + (col - center_col) ** 2)
    return 1 / (1 + d / L)

# Shape of the image
rows, cols = myArr.shape
center_row, center_col = rows / 2, cols / 2
L = 10  # Adjust this value as needed

# Create a meshgrid for row and column indices
row_indices, col_indices = np.indices(myArr.shape)

# Compute the new array using vectorized operations
myResult = distance_function(myArr, row_indices, col_indices, center_row, center_col, L)

print(myResult)
