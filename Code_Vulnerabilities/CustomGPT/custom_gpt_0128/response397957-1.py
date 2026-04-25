
import numpy as np
import cv2

# Create a sample 2D numpy array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of (x, y) coordinates
y_indices, x_indices = np.indices((rows, cols))

# Calculate the Euclidean distance from the center
d = np.sqrt((x_indices - center_col)**2 + (y_indices - center_row)**2)

# Define the L constant (this can be adjusted)
L = np.max(d)

# Apply the function to get the result based on distance
result = 1 / (1 + d / L)

# Print the result
print(result)
