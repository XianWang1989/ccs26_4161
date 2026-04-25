
import numpy as np

# Sample 2D array representing an image
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_x, center_y = cols // 2, rows // 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distance = np.sqrt((x_indices - center_x) ** 2 + (y_indices - center_y) ** 2)

# Define your function based on the distance
L = 1  # Example length scale
result = 1 / (1 + distance / L)

# Print the result
print(result)
