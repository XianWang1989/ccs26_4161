
import numpy as np

# Example 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center of the array
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of coordinates
x_coords = np.arange(rows).reshape(-1, 1)  # Vertical coordinate
y_coords = np.arange(cols)  # Horizontal coordinate

# Calculate the Euclidean distance from the center
d = np.sqrt((x_coords - center_row)**2 + (y_coords - center_col)**2)

# Example parameter L
L = 10

# Calculate the result using the provided function
result = 1 / (1 + d / L)

print("Distance Array:\n", d)
print("Result Array:\n", result)
