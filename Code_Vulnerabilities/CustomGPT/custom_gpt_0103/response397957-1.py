
import numpy as np

# Sample 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
height, width = myArr.shape

# Calculate the center coordinates
center_y, center_x = height // 2, width // 2

# Generate coordinate grids
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_x)**2 + (y_indices - center_y)**2)

# Define the function that utilizes the distances
L = 1  # Example value for L
result = 1 / (1 + distances / L)

# Output the result
print("Distances:\n", distances)
print("Result:\n", result)
