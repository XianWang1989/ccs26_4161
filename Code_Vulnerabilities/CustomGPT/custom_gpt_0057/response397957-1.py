
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of coordinates
row_indices, col_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the scaling factor
L = 1  # Set this to your desired value

# Apply the function to each element
myResult = 1 / (1 + distances / L)

# Output the result
print("Original Array:\n", myArr)
print("Distance from Center Result:\n", myResult)
