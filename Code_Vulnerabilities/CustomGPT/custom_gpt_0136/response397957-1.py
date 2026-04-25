
import numpy as np

# Dummy image array (2D pixel array)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = rows // 2, cols // 2

# Create a grid of coordinates
row_indices, col_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((row_indices - center_row)**2 + (col_indices - center_col)**2)

# Define the distance function based on your requirement
L = 1  # Define L here as needed
result = 1 / (1 + distances / L)

print("Distance from center:\n", distances)
print("Resulting image:\n", result)
