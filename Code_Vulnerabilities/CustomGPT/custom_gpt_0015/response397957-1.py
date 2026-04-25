
import numpy as np

# Create a sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center of the array
center_row, center_col = rows // 2, cols // 2

# Create coordinate grids for the array
x = np.arange(rows).reshape((rows, 1))  # Row indices
y = np.arange(cols).reshape((1, cols))  # Column indices

# Calculate the Euclidean distance from the center for each pixel
d = np.sqrt((x - center_row)**2 + (y - center_col)**2)

# Define the parameter L (you can set it based on your needs)
L = 1.0  # Example value for L

# Apply the function f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + d / L)

print("Original Array:")
print(myArr)
print("Distance from center:")
print(d)
print("Result after applying function f(i, j):")
print(result)
