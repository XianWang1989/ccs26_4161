
import numpy as np

# Sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
height, width = myArr.shape

# Calculate the center
center_row, center_col = height / 2, width / 2

# Create a grid of row and column indices
rows = np.arange(height).reshape(-1, 1)  # Shape (height, 1)
cols = np.arange(width).reshape(1, -1)    # Shape (1, width)

# Calculate the Euclidean distance from the center
distances = np.sqrt((rows - center_row) ** 2 + (cols - center_col) ** 2)

# Set a value for L (scale factor)
L = 5.0

# Apply the function
result = 1 / (1 + distances / L)

print(result)
