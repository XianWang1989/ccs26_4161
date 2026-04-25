
import numpy as np

# Create a sample 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Generate row and column indices
row_indices = np.arange(rows).reshape((rows, 1))  # Make it a column vector
col_indices = np.arange(cols).reshape((1, cols))  # Make it a row vector

# Calculate the distances from the center
d = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define your function that uses the distance
L = 1  # Example constant
def myFunc(d):
    return 1 / (1 + d / L)

# Apply the function to the distance array
myResult = myFunc(d)

print("Original array:\n", myArr)
print("Distance array:\n", d)
print("Resultant array:\n", myResult)
