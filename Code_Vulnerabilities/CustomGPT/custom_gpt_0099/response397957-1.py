
import numpy as np

# Create a sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows // 2, cols // 2

# Create an array of coordinates
x_coords = np.arange(cols)
y_coords = np.arange(rows)
x_grid, y_grid = np.meshgrid(x_coords, y_coords)

# Compute the Euclidean distance from the center
d = np.sqrt((x_grid - center_col) ** 2 + (y_grid - center_row) ** 2)

# Define L (a constant, you can adjust it)
L = 5

# Apply the function f(i, j)
result = 1 / (1 + d / L)

print("Original Array:")
print(myArr)
print("\nDistance from center (result):")
print(result)
