
import numpy as np

# Example 2D array (pixel values)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define the dimensions
rows, cols = myArr.shape

# Calculate the center of the array
center_x, center_y = cols // 2, rows // 2

# Create a grid of coordinates (row indices and col indices)
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_x) ** 2 + (y_indices - center_y) ** 2)

# Define the constant L
L = 1  # Change as needed

# Apply the function: f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + distances / L)

print("Resulting Array:")
print(result)
