
import numpy as np

# Example array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create coordinate arrays
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Set a value for L
L = 5  # you can modify this

# Apply your function to calculate the result
myResult = 1 / (1 + distances / L)

print("Original Array:")
print(myArr)
print("Distances from the center:")
print(distances)
print("Resulting Array after applying the function:")
print(myResult)
