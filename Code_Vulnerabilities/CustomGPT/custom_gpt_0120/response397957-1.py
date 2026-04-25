
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get dimensions of the array
rows, cols = myArr.shape
center_row, center_col = rows // 2, cols // 2
L = 1  # Set your own scale factor

# Create a grid of row and column indices
row_indices, col_indices = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

# Compute the Euclidean distance from the center
distances = np.sqrt((row_indices - center_row)**2 + (col_indices - center_col)**2)

# Define the function to apply
def myFunc(val, distance):
    return 1 / (1 + distance / L)

# Apply the function using vectorized operations
myResult = myFunc(myArr, distances)

print(myResult)
