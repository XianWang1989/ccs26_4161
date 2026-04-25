
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create coordinate grids
y_indices, x_indices = np.indices(myArr.shape)

# Compute the Euclidean distance from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define the function
L = 1  # Example constant
def myFunc(d):
    return 1 / (1 + d / L)

# Apply the function using vectorized operations
myResult = myFunc(distances)

print(myResult)
