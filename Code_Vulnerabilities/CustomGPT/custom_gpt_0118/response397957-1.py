
import numpy as np

# Example array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Image dimensions
rows, cols = myArr.shape
center_row, center_col = rows / 2, cols / 2

# Create mesh grids for row and column indices
x_indices, y_indices = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

# Calculate Euclidean distance from the center
distances = np.sqrt((x_indices - center_row) ** 2 + (y_indices - center_col) ** 2)

# Define the function to compute the desired output
def myFunc(val, d, L):
    return 1 / (1 + d / L)

# Specify L (e.g., a constant)
L = np.max(distances)  # You can choose an appropriate value for L

# Apply the function using element-wise operations
myResult = myFunc(myArr, distances, L)

print("Original Array:\n", myArr)
print("Result Array:\n", myResult)
