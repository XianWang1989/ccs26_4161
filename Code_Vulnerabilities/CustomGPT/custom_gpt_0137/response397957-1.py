
import numpy as np

# Example 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Dimension of the array
rows, cols = myArr.shape

# Define the length L for the function
L = 10

# Calculate the center of the image
center_row = rows / 2
center_col = cols / 2

# Create a grid of row and column indices
Y, X = np.ogrid[:rows, :cols]

# Calculate Euclidean distance from the center
d = np.sqrt((X - center_col)**2 + (Y - center_row)**2)

# Apply the function f(i, j) = 1/(1 + d(i,j)/L)
myResult = 1 / (1 + d / L)

print("Original Array:\n", myArr)
print("Distance from Center:\n", d)
print("Result Array:\n", myResult)
