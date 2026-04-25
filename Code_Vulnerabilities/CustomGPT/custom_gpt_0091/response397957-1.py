
import numpy as np

# Define the array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define the parameter L (can be any positive value)
L = 1.0

# Compute the desired function for each pixel
myResult = 1 / (1 + distances / L)

print("Original Array:\n", myArr)
print("Distances:\n", distances)
print("Resulting Array:\n", myResult)
