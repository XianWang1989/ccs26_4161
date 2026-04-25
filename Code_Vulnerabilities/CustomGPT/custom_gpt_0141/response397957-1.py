
import numpy as np
import cv2

# Sample 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the image
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create arrays of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Define your function based on the distance
L = 1  # You can set L as needed
result = 1 / (1 + distances / L)

# Print the result
print("Original Array:\n", myArr)
print("Distances from center:\n", distances)
print("Result after applying f(i, j):\n", result)
