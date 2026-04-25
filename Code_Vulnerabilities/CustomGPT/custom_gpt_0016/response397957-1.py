
import numpy as np

# Create a sample 2D pixel array (e.g., an image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array to determine its size
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of coordinates (row, col)
x_indices, y_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_row) ** 2 + (y_indices - center_col) ** 2)

# Define the constant L (you can adjust this value)
L = 5

# Apply the function for each pixel based on the distance
# f(i, j) = 1 / (1 + d(i, j) / L)
result = 1 / (1 + distances / L)

print("Original Array:\n", myArr)
print("Distances from Center:\n", distances)
print("Result Array:\n", result)
