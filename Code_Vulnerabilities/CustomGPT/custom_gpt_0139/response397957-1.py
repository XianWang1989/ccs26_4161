
import numpy as np

# Example 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Image dimensions
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center point
distances = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Define L
L = 10  # Example value

# Apply the function to each pixel using broadcasting
myResult = 1 / (1 + distances / L)

print(myResult)
