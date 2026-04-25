
import numpy as np

# Example 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = rows / 2, cols / 2

# Create grid of coordinates (row, col)
x = np.arange(rows)
y = np.arange(cols)
xx, yy = np.meshgrid(x, y, indexing='ij')

# Compute the Euclidean distance from the center
d = np.sqrt((xx - center_row)**2 + (yy - center_col)**2)

# Define the function
L = 10  # You can set this to any desired value
f = lambda d: 1 / (1 + d / L)

# Apply the function to the distance array
myResult = f(d)

print(myResult)
