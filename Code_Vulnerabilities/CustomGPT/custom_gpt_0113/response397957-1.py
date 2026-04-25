
import numpy as np

# Sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row = rows / 2
center_col = cols / 2

# Create a grid of (row, col) coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate Euclidean distance from the center for each pixel
d = np.sqrt((y_indices - center_row)**2 + (x_indices - center_col)**2)

# Specify the L value (for example, L = 1)
L = 1

# Calculate the result using the specified function
result = 1 / (1 + d / L)

print(result)
