
import numpy as np

# Example image array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows // 2, cols // 2

# Create a grid of coordinates
x = np.arange(rows).reshape((rows, 1))  # column vector
y = np.arange(cols).reshape((1, cols))  # row vector

# Calculate the Euclidean distance from the center
d = np.sqrt((x - center_row)**2 + (y - center_col)**2)

# Define the constant L
L = 10  # Example constant for normalization

# Apply the function to calculate the result
myResult = 1 / (1 + d / L)

print(myResult)
