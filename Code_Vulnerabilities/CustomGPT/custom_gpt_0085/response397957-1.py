
import numpy as np

# Sample 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create coordinate grids
x = np.arange(rows).reshape(-1, 1)  # Column vector for rows
y = np.arange(cols).reshape(1, -1)  # Row vector for columns

# Calculate Euclidean distance from the center
d = np.sqrt((x - center_row) ** 2 + (y - center_col) ** 2)

# Define the parameter L (you can adjust this value)
L = 5

# Apply the function: f(i, j) = 1 / (1 + d(i, j) / L)
myResult = 1 / (1 + d / L)

# Print the result
print(myResult)
