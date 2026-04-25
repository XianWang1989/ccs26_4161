
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row = rows / 2
center_col = cols / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define L (a constant for normalization)
L = np.max(distances)  # or any other value you want to use for L

# Apply the function f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + distances / L)

print("Distances from center:\n", distances)
print("Result of the function:\n", result)
