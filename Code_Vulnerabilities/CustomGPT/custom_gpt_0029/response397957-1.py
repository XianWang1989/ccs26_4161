
import numpy as np

# Example 2D array representing pixel values
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Image dimensions
rows, cols = myArr.shape

# Determine the center of the image
center_row, center_col = rows / 2, cols / 2

# Create a mesh grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define L (you can set this based on your specific requirements)
L = 1  # Example value

# Apply the function f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + distances / L)

print(result)
