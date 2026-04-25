
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Image dimensions
rows, cols = myArr.shape
center = np.array([(rows - 1) / 2, (cols - 1) / 2])

# Create a grid of (row, col) coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((y_indices - center[0])**2 + (x_indices - center[1])**2)

# Set the parameter L (you can modify this value)
L = 1.0  # Example value

# Applying the function f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + distances / L)

print("Resulting array:")
print(result)
