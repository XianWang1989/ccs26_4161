
import numpy as np

# Create a sample 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Compute the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a meshgrid of row and column indices
row_indices, col_indices = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

# Compute the Euclidean distance from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define your function that uses the distance
L = 1  # You can set your desired value for L
f = 1 / (1 + distances / L)

# f now contains the values for each pixel based on the distance calculated
print(f)
