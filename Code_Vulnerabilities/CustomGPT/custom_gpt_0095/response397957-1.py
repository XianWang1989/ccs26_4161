
import numpy as np
import cv2

# Define your array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Image dimensions
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of row and column coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate Euclidean distances from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define L (a constant for scaling distances)
L = 5

# Apply the function f(i, j) = 1 / (1 + d(i, j) / L)
myResult = 1 / (1 + distances / L)

print(myResult)
