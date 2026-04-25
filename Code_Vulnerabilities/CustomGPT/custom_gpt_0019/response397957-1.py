
import numpy as np

# Example 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Image dimensions
rows, cols = myArr.shape
center_row, center_col = rows / 2, cols / 2

# Create meshgrid of row and column indices
row_indices, col_indices = np.indices(myArr.shape)

# Calculate Euclidean distance from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the function f(i, j)
L = 10  # Example value for L
def myFunc(distance):
    return 1 / (1 + distance / L)

# Apply the function to the distances
myResult = myFunc(distances)

print(myResult)
