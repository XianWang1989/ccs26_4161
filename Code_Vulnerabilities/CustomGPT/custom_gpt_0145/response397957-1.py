
import numpy as np

# Define the pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of coordinates (row indices and column indices)
row_indices, col_indices = np.indices(myArr.shape)

# Calculate the Euclidean distances from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the function to apply
L = 1  # Example value for L
def f(d):
    return 1 / (1 + d / L)

# Apply the function to the distances
myResult = f(distances)

print("Original Array:")
print(myArr)
print("\nDistances from the center:")
print(distances)
print("\nResult Array:")
print(myResult)
