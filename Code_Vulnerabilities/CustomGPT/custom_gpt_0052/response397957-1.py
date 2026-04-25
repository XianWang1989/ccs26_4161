
import numpy as np

# Create a sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array to determine the center
rows, cols = myArr.shape
center_row, center_col = rows // 2, cols // 2

# Create a grid of row and column indices
y_indices, x_indices = np.indices((rows, cols))

# Calculate the Euclidean distance from the center
d = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Define the scaling factor L
L = 5  # Example value for L

# Calculate the function f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + d / L)

print(result)
