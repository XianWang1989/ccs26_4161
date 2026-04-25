
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center = (rows - 1) / 2, (cols - 1) / 2

# Create coordinate arrays
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
d = np.sqrt((x_indices - center[1]) ** 2 + (y_indices - center[0]) ** 2)

# Define the function
L = 1  # Set your L value here
result = 1 / (1 + d / L)

print(result)
