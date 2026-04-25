
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Define the function
def myFunc(val, row, col, L):
    # Calculate the center coordinates
    center_row, center_col = (rows - 1) / 2, (cols - 1) / 2
    # Calculate the Euclidean distance from the center
    distance = np.sqrt((row - center_row) ** 2 + (col - center_col) ** 2)
    return 1 / (1 + distance / L)

# Create coordinate arrays
row_indices, col_indices = np.indices(myArr.shape)

# Define L (for example)
L = 2.0

# Vectorized evaluation of myFunc
myResult = myFunc(myArr, row_indices, col_indices, L)

print(myResult)
