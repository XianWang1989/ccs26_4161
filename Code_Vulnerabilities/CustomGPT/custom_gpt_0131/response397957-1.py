
import numpy as np
import cv2

# Create a sample 2D array (image) - for example, a 5x5 image
myArr = np.array([[0, 1, 2, 3, 4],
                  [5, 6, 7, 8, 9],
                  [10, 11, 12, 13, 14],
                  [15, 16, 17, 18, 19],
                  [20, 21, 22, 23, 24]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = rows // 2, cols // 2
L = 10  # A sample value for L

# Create meshgrid for row and column indices
x_indices, y_indices = np.indices(myArr.shape)

# Compute the Euclidean distance from each point to the center
d = np.sqrt((x_indices - center_row) ** 2 + (y_indices - center_col) ** 2)

# Apply the function: f(i, j) = 1/(1 + d(i, j)/L)
myResult = 1 / (1 + d / L)

# Print the result
print(myResult)
