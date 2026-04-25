
import numpy as np
import cv2

# Define your 2D numpy array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create coordinate grids
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distances from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define your distance function
L = 5  # You can set L to a desired value
f = 1 / (1 + distances / L)

# Optionally apply the function to the original array values
result = f * myArr

# Display the results
print("Distance from center:\n", distances)
print("Function result:\n", result)
