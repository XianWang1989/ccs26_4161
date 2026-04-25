
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Determine the center of the image
rows, cols = myArr.shape
center_row, center_col = rows // 2, cols // 2

# Create meshgrid for row and column indices
row_indices, col_indices = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

# Calculate Euclidean distance from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the function to apply
def myFunc(value, distance, L):
    return 1 / (1 + distance / L)

# Set L (distance scale factor)
L = 10  # Example value, adjust as needed

# Apply the function using broadcasting
myResult = myFunc(myArr, distances, L)

print("Resulting array:\n", myResult)
