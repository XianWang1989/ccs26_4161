
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center position
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of row and column indices
row_indices, col_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the parameter L
L = 10  # Example value for L

# Apply the function f(i, j)
myResult = 1 / (1 + distances / L)

print(myResult)
