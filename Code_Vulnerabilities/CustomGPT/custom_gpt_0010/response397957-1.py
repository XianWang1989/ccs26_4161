
import numpy as np

# Sample 2D pixel array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Calculate the dimensions of the array
rows, cols = myArr.shape

# Find the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of coordinates
x_indices = np.arange(rows).reshape((rows, 1))  # Column vector
y_indices = np.arange(cols).reshape((1, cols))  # Row vector

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_row) ** 2 + (y_indices - center_col) ** 2)

# Parameter L (can be changed as needed)
L = np.max(distances)  # Use maximum distance for normalization, for example

# Compute the result using the given function
myResult = 1 / (1 + distances / L)

print("Original Array:\n", myArr)
print("Distance Matrix:\n", distances)
print("Resulting Array:\n", myResult)
