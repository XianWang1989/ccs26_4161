
import numpy as np

# Sample 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Determine the center coordinates
rows, cols = myArr.shape
center_row, center_col = rows / 2, cols / 2

# Create coordinate arrays
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the distance from the center
d = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define your function
L = 10  # Example constant
result = 1 / (1 + d / L)

print(result)
