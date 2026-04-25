
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a meshgrid of row and column indices
row_indices, col_indices = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

# Calculate the distance from the center for each pixel
d = np.sqrt((row_indices - center_row)**2 + (col_indices - center_col)**2)

# Assume L is some constant, for example:
L = 1.0  # You can adjust L based on your requirement

# Calculate the function for each pixel
result = 1 / (1 + d / L)

# Display the result
print(result)
