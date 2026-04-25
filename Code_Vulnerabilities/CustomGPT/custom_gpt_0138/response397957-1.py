
import numpy as np

# Define the pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array to determine the center
rows, cols = myArr.shape
center_row, center_col = rows // 2, cols // 2

# Create a grid of coordinates
row_indices, col_indices = np.indices(myArr.shape)

# Compute the Euclidean distance from the center
distance = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Parameter L
L = 1  # or any value you want

# Apply the function
def myFunc(d, L):
    return 1 / (1 + d / L)

# Calculate the final result
myResult = myFunc(distance, L)

print(myResult)
