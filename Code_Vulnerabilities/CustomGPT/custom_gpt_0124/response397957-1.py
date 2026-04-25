
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row = rows // 2
center_col = cols // 2

# Create a grid of row and column indices
row_indices = np.arange(rows)[:, np.newaxis]  # Shape (rows, 1)
col_indices = np.arange(cols)                  # Shape (cols,)

# Calculate distances from the center
d = np.sqrt((row_indices - center_row)**2 + (col_indices - center_col)**2)

# Define the constant L (example value)
L = 10.0

# Apply the function to calculate the result
result = 1 / (1 + d / L)

print("Distance from center:\n", d)
print("Result:\n", result)
