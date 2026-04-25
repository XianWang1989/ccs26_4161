
import numpy as np

# Example pixel array (2D)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
height, width = myArr.shape

# Find the center coordinates
center_y, center_x = height / 2, width / 2

# Create meshgrid of row and column indices
X, Y = np.meshgrid(np.arange(width), np.arange(height))

# Calculate the Euclidean distance from the center for each pixel
distances = np.sqrt((X - center_x) ** 2 + (Y - center_y) ** 2)

# Define the L parameter
L = np.max(distances)  # Example: Normalize by the maximum distance

# Implement the function f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + distances / L)

print("Original Array:\n", myArr)
print("Distances from center:\n", distances)
print("Result:\n", result)
