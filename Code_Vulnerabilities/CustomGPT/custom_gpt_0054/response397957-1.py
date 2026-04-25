
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row = rows / 2
center_col = cols / 2

# Create coordinate arrays
x_indices, y_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_row)**2 + (y_indices - center_col)**2)

# Define the L value as required for your specific use case
L = 2  # example value

# Apply the function to compute the result for each pixel
myResult = 1 / (1 + distances / L)

print(myResult)
