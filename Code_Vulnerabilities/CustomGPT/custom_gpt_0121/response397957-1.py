
import numpy as np

# Example image array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate distances from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define the L value (e.g. maximum distance for normalization)
L = np.max(distances)

# Calculate the result using the desired function
myResult = 1 / (1 + distances / L)

print("Distances from center:")
print(distances)
print("Result after applying the function:")
print(myResult)
