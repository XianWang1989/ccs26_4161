
import numpy as np

# Create a sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Compute the center of the image (assuming the center is the point (rows/2, cols/2))
center_row = rows / 2
center_col = cols / 2

# Create arrays of row indices and col indices
row_indices = np.arange(rows).reshape(rows, 1)  # Shape (rows, 1)
col_indices = np.arange(cols).reshape(1, cols)  # Shape (1, cols)

# Compute the distance from the center for all pixel coordinates
d = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define L (the scale factor for the distance)
L = 1  # You can choose any appropriate scale for your application

# Apply the distance function
# f(i, j) = 1 / (1 + d(i, j)/L)
myResult = 1 / (1 + d / L)

# Display the original array and the result
print("Original Array:")
print(myArr)
print("\nDistance Function Result:")
print(myResult)
