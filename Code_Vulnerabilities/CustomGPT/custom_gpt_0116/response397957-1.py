
import numpy as np

# Sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the image
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
d = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Define the L parameter
L = 1  # Example value for L

# Compute the function: f(i, j) = 1 / (1 + d(i, j) / L)
myResult = 1 / (1 + d / L)

print(myResult)
