
import numpy as np

# Define your array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create arrays of the row and column indices
row_indices, col_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center for all pixels
d = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define your function that takes the original value and distance
L = 1  # You can set this to whatever your length scale is
def myFunc(val, distance):
    return 1 / (1 + distance / L)

# Apply the function across the whole array
myResult = myFunc(myArr, d)

print(myResult)
