
import numpy as np

# Sample pixel array (2D)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array to find its center
rows, cols = myArr.shape
center_row, center_col = rows // 2, cols // 2

# Create a grid of coordinates
row_indices = np.arange(rows).reshape((rows, 1))
col_indices = np.arange(cols).reshape((1, cols))

# Calculate the Euclidean distance from the center
d = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# You can define your function based on d
L = 10  # Example constant
result = 1 / (1 + d / L)

print(result)
