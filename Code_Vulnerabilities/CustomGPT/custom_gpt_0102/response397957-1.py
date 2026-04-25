
import numpy as np

# Sample 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Parameters
L = 10.0
rows, cols = myArr.shape
center_row, center_col = rows / 2, cols / 2

# Calculate distances from the center
y_indices, x_indices = np.indices(myArr.shape)

# Euclidean distance from the center
d = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Apply the function
myResult = 1 / (1 + d / L)

print(myResult)
