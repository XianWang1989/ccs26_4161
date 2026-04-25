
import numpy as np

# Define your image array and parameters
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])
L = 2  # some arbitrary length

# Calculate the center of the image
rows, cols = myArr.shape
center = (rows - 1) / 2, (cols - 1) / 2

# Create coordinate grid using np.indices
x_indices, y_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
d = np.sqrt((x_indices - center[0])**2 + (y_indices - center[1])**2)

# Calculate the result using the function defined
myResult = 1 / (1 + d / L)

print(myResult)
