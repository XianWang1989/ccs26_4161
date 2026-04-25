
import numpy as np

# Sample image array (e.g., 3x3 pixel values)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create arrays of row and column indices
row_indices = np.arange(rows).reshape(rows, 1)  # Shape (rows, 1)
col_indices = np.arange(cols).reshape(1, cols)  # Shape (1, cols)

# Calculate Euclidean distances from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the function based on the distance
L = 1  # Example constant for scaling (adjust as needed)
result = 1 / (1 + distances / L)

print("Distance Map:\n", distances)
print("Resulting Transformation:\n", result)
