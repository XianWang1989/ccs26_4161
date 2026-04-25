
import numpy as np

# Example array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Dimensions
rows, cols = myArr.shape
center = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of coordinates
y_indices, x_indices = np.mgrid[0:rows, 0:cols]

# Calculate Euclidean distance from the center
d = np.sqrt((x_indices - center[1])**2 + (y_indices - center[0])**2)

# Define your function
L = 10  # Example parameter
f = 1 / (1 + d / L)

# Result
myResult = f

print(myResult)
