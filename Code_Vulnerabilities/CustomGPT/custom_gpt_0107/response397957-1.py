
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create an array of row and column indices
row_indices = np.arange(rows).reshape(-1, 1)  # Shape (rows, 1)
col_indices = np.arange(cols).reshape(1, -1)  # Shape (1, cols)

# Calculate d(i, j) using broadcasting
d = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the constant L (threshold value)
L = 5.0  # Change as needed

# Calculate the output function f(i, j)
result = 1 / (1 + d / L)

print("Distance from center:\n", d)
print("Result:\n", result)
