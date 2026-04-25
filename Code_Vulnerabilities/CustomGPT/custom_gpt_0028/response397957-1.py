
import numpy as np

# Create a sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Compute the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create meshgrid for row and column coordinates
row_indices, col_indices = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

# Compute the Euclidean distance from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the function to apply
L = 5  # Example constant L
def myFunc(d):
    return 1 / (1 + d / L)

# Apply the function vectorized
myResult = myFunc(distances)

print("Original Array:\n", myArr)
print("Distance Result:\n", myResult)
