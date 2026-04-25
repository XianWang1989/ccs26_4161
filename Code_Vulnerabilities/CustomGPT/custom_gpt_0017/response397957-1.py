
import numpy as np

# Sample 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define the image dimensions
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create grids of row and column indices
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Define your function that depends on the distance
L = 1.0  # some constant value
def distance_function(d):
    return 1 / (1 + d / L)

# Apply the function to the distances
myResult = distance_function(distances)

# Display the result
print(myResult)
