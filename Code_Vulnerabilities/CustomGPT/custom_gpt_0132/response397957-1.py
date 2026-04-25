
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get shape of array
rows, cols = myArr.shape

# Determine the center of the array
center_row, center_col = rows / 2, cols / 2

# Create a meshgrid for the row and column indices
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distance = np.sqrt((y_indices - center_row)**2 + (x_indices - center_col)**2)

# Define L (for normalization)
L = np.max(distance)  # or any other value depending on your application

# Calculate the result using the given formula
result = 1 / (1 + distance / L)

print(result)
