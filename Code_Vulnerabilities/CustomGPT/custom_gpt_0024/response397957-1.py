
import numpy as np

# Define the image array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
height, width = myArr.shape

# Calculate the center coordinates
center_row, center_col = height / 2, width / 2

# Generate grid of coordinates
row_indices = np.arange(height).reshape(height, 1)  # Shape: (height, 1)
col_indices = np.arange(width).reshape(1, width)    # Shape: (1, width)

# Calculate the distance from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Set L (a constant for scaling the distance)
L = np.max(distances)

# Define the function to apply to each pixel
def myFunc(d):
    return 1 / (1 + d / L)

# Vectorize the function and apply it to the distances
myResult = myFunc(distances)

print(myResult)
