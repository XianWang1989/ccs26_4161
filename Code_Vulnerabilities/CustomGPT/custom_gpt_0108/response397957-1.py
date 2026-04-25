
import numpy as np

# Create the pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create arrays for row and column indices
row_indices = np.arange(rows).reshape(-1, 1)  # Column vector
col_indices = np.arange(cols)  # Row vector

# Calculate the Euclidean distances from the center
d = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define L (a constant for scaling, adjust as necessary)
L = 10  # Example value for L

# Apply the function f(i, j)
result = 1 / (1 + d / L)

print("Distance from Center:\n", d)
print("Resulting Array:\n", result)
