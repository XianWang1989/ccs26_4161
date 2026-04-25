
import numpy as np

# Create a sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the image
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of coordinates
Y, X = np.indices(myArr.shape)

# Calculate the Euclidean distance from each pixel to the center
d = np.sqrt((X - center_col)**2 + (Y - center_row)**2)

# Constant L (you can adjust this value)
L = 5

# Apply the function f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + d / L)

print(result)
