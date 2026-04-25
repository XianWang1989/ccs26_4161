
import numpy as np

# Example 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Generate grid of row and column indices
r, c = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
d = np.sqrt((r - center_row) ** 2 + (c - center_col) ** 2)

# Define the function to apply
L = 1  # Example value for L
result = 1 / (1 + d / L)

print(result)
