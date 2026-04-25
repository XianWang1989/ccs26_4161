
import numpy as np
import cv2

# Create an example image array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get image dimensions
rows, cols = myArr.shape
center_row, center_col = rows / 2, cols / 2

# Create a grid of (row, col) coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
d = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Define your function
L = 1.0  # Define L as per your requirement
myFunc = lambda d: 1 / (1 + d / L)

# Apply the function to the distance array
myResult = myFunc(d)

# Print the resulting output
print(myResult)
