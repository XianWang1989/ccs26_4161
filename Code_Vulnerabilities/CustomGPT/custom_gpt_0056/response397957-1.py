
import numpy as np

# Example pixel array (2D)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Define the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create coordinate arrays
row_indices = np.arange(rows).reshape(rows, 1)  # Shape (rows, 1)
col_indices = np.arange(cols).reshape(1, cols)  # Shape (1, cols)

# Calculate distance from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the function using the distances
L = 1.0  # Set your L parameter
f = 1 / (1 + distances / L)

# Result
print("Distance Matrix:\n", distances)
print("Function Result:\n", f)
