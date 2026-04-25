
import numpy as np

# Create a sample 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of coordinates
row_indices, col_indices = np.indices(myArr.shape)

# Compute the Euclidean distance from the center for each pixel
d = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Parameter for your function
L = 5  # Example value; adjust as needed

# Apply the function to calculate the result for each pixel
myResult = 1 / (1 + d / L)

print(myResult)
