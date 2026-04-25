
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array to find the center
rows, cols = myArr.shape
center = (rows - 1) / 2, (cols - 1) / 2  # Coordinates of the center

# Calculate the distance function
def distance_function(val, row, col, L):
    d = np.sqrt((row - center[0]) ** 2 + (col - center[1]) ** 2)
    return 1 / (1 + d / L)

# Create a grid of indices (row and column)
row_indices, col_indices = np.indices(myArr.shape)

# Vectorizing the distance function
L = 1  # Change this value as necessary
myResult = distance_function(myArr, row_indices, col_indices, L)

print(myResult)
