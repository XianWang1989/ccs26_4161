
import numpy as np

# Example 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Define the center points
center_row, center_col = rows / 2, cols / 2

# Create a grid of indices for the pixel coordinates
row_indices = np.arange(rows)
col_indices = np.arange(cols)

# Use np.meshgrid to create a coordinate grid
x, y = np.meshgrid(col_indices, row_indices)

# Calculate the Euclidean distance from the center
d = np.sqrt((y - center_row) ** 2 + (x - center_col) ** 2)

# Define the parameter L, which can be adjusted as needed
L = 2.0  # Example value

# Apply the distance function on the pixel distances
myResult = 1 / (1 + d / L)

# Display the result
print(myResult)
