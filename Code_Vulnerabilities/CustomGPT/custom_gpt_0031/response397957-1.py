
import numpy as np

# Create a sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center of the array
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create coordinate grids
y_indices, x_indices = np.indices((rows, cols))

# Calculate the Euclidean distance from the center
d = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Define the parameter L (you can set this to any value you need)
L = 2.0  # Example value

# Apply the function f(i, j) = 1 / (1 + d(i, j) / L) in a vectorized manner
myResult = 1 / (1 + d / L)

print(myResult)
