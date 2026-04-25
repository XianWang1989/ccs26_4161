
import numpy as np

# Sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create grid of coordinates
row_indices = np.arange(rows)[:, np.newaxis]  # Make it a column vector
col_indices = np.arange(cols)                  # Row vector

# Calculate Euclidean distances from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define your function f(i, j) = 1/(1 + d(i, j)/L)
L = 5  # Example value for L
myResult = 1 / (1 + distances / L)

print(myResult)
