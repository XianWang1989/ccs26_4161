
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate center coordinates
center_x, center_y = cols / 2, rows / 2

# Create an array of row indices and column indices
y_indices, x_indices = np.indices(myArr.shape)

# Calculate Euclidean distance from the center
d = np.sqrt((x_indices - center_x) ** 2 + (y_indices - center_y) ** 2)

# Define your function to apply
L = 1  # Example value for L (you may want to adjust it as needed)
def myFunc(val, dist):
    return 1 / (1 + dist / L)

# Use np.vectorize to apply the function
myResult = np.vectorize(myFunc)(myArr, d)

print(myResult)
