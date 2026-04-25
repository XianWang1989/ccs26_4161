
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Center coordinates
center_row, center_col = rows / 2, cols / 2

# Create row and column indices
row_indices, col_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center for each pixel
d = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define your function
L = 5  # Example value for L
myFunc = lambda d: 1 / (1 + d / L)

# Vectorize the function and apply it to the distance array
myResult = myFunc(d)

print(myResult)
