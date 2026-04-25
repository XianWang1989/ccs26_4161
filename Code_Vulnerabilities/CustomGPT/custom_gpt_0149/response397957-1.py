
import numpy as np

# Sample array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Define the length scale (L)
L = 3  # Example value

# Apply the function to each pixel
result = 1 / (1 + distances / L)

print("Original Array:")
print(myArr)
print("Distances from Center:")
print(distances)
print("Resulting Array:")
print(result)
