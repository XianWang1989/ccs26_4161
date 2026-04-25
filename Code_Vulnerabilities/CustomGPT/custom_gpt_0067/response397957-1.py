
import numpy as np

# Sample 2D numpy array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define the size of the array to find the center
rows, cols = myArr.shape
center = (rows // 2, cols // 2)

# Generate grid of coordinates
x_indices, y_indices = np.indices(myArr.shape)

# Calculate Euclidean distance from center (d(i, j))
distances = np.sqrt((x_indices - center[0])**2 + (y_indices - center[1])**2)

# L is a constant defining the scale
L = 5  # Example value

# Apply the function to calculate the result
myResult = 1 / (1 + distances / L)

print(myResult)
