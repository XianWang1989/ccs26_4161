
import numpy as np

# Your pixel array (you can replace this with your actual image data)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create coordinate grids for rows and columns
row_indices, col_indices = np.indices((rows, cols))

# Calculate the Euclidean distance from the center
distances = np.sqrt((row_indices - center_row)**2 + (col_indices - center_col)**2)

# Define the length L (you can set this value as needed)
L = 5  # Example length

# Apply your function to compute the result for each pixel
myResult = 1 / (1 + distances / L)

# Print results
print("My Array:\n", myArr)
print("Distances from center:\n", distances)
print("Resulting Array:\n", myResult)
