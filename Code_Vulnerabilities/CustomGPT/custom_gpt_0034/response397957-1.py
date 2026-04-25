
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape
center_row, center_col = rows // 2, cols // 2

# Create a grid of coordinates
row_indices, col_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
d = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the constant L
L = 1  # You can set this to any value you need

# Compute the resulting array using the distance
myResult = 1 / (1 + d / L)

print("Original Array:\n", myArr)
print("Distance Result Array:\n", myResult)
