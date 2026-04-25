
import numpy as np

# Example 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = rows / 2, cols / 2

# Create a grid of row and column indices
row_indices, col_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distance = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the scaling factor L
L = 1  # Change this as needed

# Apply the function
myResult = 1 / (1 + distance / L)

print(myResult)
