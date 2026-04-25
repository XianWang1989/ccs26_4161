
import numpy as np

# Define the 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of row and column coordinates
row_indices, col_indices = np.indices(myArr.shape)

# Calculate Euclidean distance from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the function that uses distances
def myFunc(d, L):
    return 1 / (1 + d / L)

# Example value for L
L = 2.0

# Apply the function
myResult = myFunc(distances, L)

# Output the result
print(myResult)
