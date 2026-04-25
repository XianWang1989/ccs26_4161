
import numpy as np

# Example 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Dimensions of the array
height, width = myArr.shape

# Center of the image
center_row, center_col = height / 2, width / 2

# Create coordinate grids
x_indices, y_indices = np.indices(myArr.shape)

# Compute Euclidean distances from the center
distances = np.sqrt((x_indices - center_row) ** 2 + (y_indices - center_col) ** 2)

# Set the value of L (Distance scaling factor)
L = np.max(distances)

# Implementing the function f(i, j)
result = 1 / (1 + distances / L)

# Output result
print(result)
