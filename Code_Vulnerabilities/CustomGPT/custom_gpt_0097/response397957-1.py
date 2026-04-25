
import numpy as np

# Define the pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Generate grid of row and column indices
row_indices, col_indices = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

# Calculate distances from the center
distances = np.sqrt((row_indices - center_row)**2 + (col_indices - center_col)**2)

# Define the function to apply
L = 5  # Example constant
def myFunc(d):
    return 1 / (1 + d / L)

# Apply the function to the distances
myResult = myFunc(distances)

print(myResult)
