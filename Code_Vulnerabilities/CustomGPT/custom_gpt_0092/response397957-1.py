
import numpy as np

# Create the example array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define the parameters
L = 5  # Example parameter for distance function
rows, cols = myArr.shape
center_row, center_col = rows / 2, cols / 2

# Create a grid of row and column indices
row_indices, col_indices = np.indices(myArr.shape)

# Calculate the distances from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Apply the function to each distance
myResult = 1 / (1 + distances / L)

print("Distance from center:\n", distances)
print("Resulting array:\n", myResult)
