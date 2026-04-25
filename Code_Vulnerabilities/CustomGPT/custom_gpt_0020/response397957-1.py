
import numpy as np

# Example 2D pixel array (grayscale image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Calculate the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the distance from the center for each pixel
distances = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# The length scale for distance normalization
L = 5  # This can be adjusted based on your requirements

# Calculate the desired function f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + distances / L)

print("Distance from center:\n", distances)
print("Resulting function values:\n", result)
