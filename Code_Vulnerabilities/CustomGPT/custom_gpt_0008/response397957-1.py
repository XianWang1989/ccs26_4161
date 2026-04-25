
import numpy as np

# Define your 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of row and column indices
row_indices, col_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center for each pixel
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the function using the distances
L = 1  # Example value for L
f = 1 / (1 + distances / L)

# Resulting array with the function applied
myResult = f * myArr

print(myResult)
