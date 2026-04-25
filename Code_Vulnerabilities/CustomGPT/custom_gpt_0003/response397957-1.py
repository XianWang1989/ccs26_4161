
import numpy as np

# Example input array, representing pixel values.
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a mesh grid for the pixel coordinates
x = np.arange(0, rows)
y = np.arange(0, cols)
xx, yy = np.meshgrid(x, y, indexing='ij')

# Calculate the Euclidean distance from the center
d = np.sqrt((xx - center_row) ** 2 + (yy - center_col) ** 2)

# Set a value for L (you may adjust this based on your requirements)
L = 10

# Apply the function f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + d / L)

print("Resulting array after distance function applied:")
print(result)
