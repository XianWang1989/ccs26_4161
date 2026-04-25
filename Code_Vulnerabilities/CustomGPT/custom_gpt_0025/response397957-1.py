
import numpy as np

# Create a sample array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of indices
y_indices, x_indices = np.indices(myArr.shape)

# Calculate distances from the center
d = np.sqrt((x_indices - center_col)**2 + (y_indices - center_row)**2)

# Define L (can be set to any positive value, e.g., image width, height, etc.)
L = 1.0

# Apply the function
myResult = 1 / (1 + d / L)

# Print the result
print(myResult)
