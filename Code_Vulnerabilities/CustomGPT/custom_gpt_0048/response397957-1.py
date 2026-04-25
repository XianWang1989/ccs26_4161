
import numpy as np

# Sample 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of row and column indices
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Set L (a constant for scaling)
L = 5  # Example value

# Apply the function f(i, j) = 1 / (1 + d(i, j) / L)
myResult = 1 / (1 + distances / L)

print(myResult)
