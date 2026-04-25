
import numpy as np

# Define the pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of row and column indices
row_indices = np.arange(rows).reshape((rows, 1))  # Shape (rows, 1)
col_indices = np.arange(cols).reshape((1, cols))  # Shape (1, cols)

# Calculate the distance from the center for each pixel
d = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define your function
L = 1  # you can set L to any value you need
f = 1 / (1 + d / L)

# Apply the function to the pixel array
myResult = f * myArr  # Or any operation you want to perform with myArr

print("Distance from Center:\n", d)
print("Result:\n", myResult)
