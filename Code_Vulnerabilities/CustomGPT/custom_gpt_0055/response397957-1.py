
import numpy as np

# Create a sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows // 2, cols // 2

# Create grid of (row, col) coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate distance from the center for each pixel
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Set L (a scaling factor for distance)
L = np.max(distances)

# Apply the function f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + distances / L)

print("Resulting array:\n", result)
