
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Dimensions of the array
rows, cols = myArr.shape

# Center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define L (a scaling factor)
L = np.max(distances)  # Example: using the max distance as L

# Calculate the desired function for each pixel
result = 1 / (1 + distances / L)

print("Distances from center:\n", distances)
print("Resulting array:\n", result)
