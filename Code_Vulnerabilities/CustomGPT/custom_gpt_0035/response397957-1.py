
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Dimensions of the array
rows, cols = myArr.shape

# Calculate center coordinates
center_row, center_col = rows / 2, cols / 2

# Generate grid of row and column indices
x_indices, y_indices = np.indices(myArr.shape)

# Calculate distances from the center
distances = np.sqrt((x_indices - center_row) ** 2 + (y_indices - center_col) ** 2)

# Define your distance function
L = 5  # Example length scale
distance_function = 1 / (1 + distances / L)

# Applying the function to the pixel array values
result = distance_function * myArr  # Example of applying the result

print("Distances from center:\n", distances)
print("Resulting values:\n", result)
