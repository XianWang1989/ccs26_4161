
import numpy as np

# Create a sample 2D numpy array (image pixel intensity)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a meshgrid for row and column indices
row_indices, col_indices = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

# Calculate the Euclidean distance from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Scale the distance for the function f(i, j) = 1/(1 + d(i, j)/L)
L = np.max(distances)  # You can set L to a different value if needed
result = 1 / (1 + distances / L)

print("Distances from center:\n", distances)
print("Resulting values:\n", result)
