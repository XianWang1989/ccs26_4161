
import numpy as np

# Define the array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define the length scale L
L = 10.0

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_x, center_y = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance of each point from the center
d = np.sqrt((x_indices - center_x) ** 2 + (y_indices - center_y) ** 2)

# Calculate the result based on the formula
myResult = 1 / (1 + d / L)

print("Original Array:")
print(myArr)
print("\nDistance from Center:")
print(d)
print("\nResulting Array:")
print(myResult)
