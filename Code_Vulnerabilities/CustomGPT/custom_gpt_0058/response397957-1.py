
import numpy as np

# Sample 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center of the image
center = np.array([rows / 2, cols / 2])

# Generate row and column indices
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the distances from the center
d = np.sqrt((x_indices - center[1])**2 + (y_indices - center[0])**2)

# Define the parameter L (set as per your requirement)
L = 5

# Apply the function f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + d / L)

# Print the result
print(result)
