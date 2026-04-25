
import numpy as np
import cv2

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Image dimensions
rows, cols = myArr.shape
center_row, center_col = rows / 2, cols / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the distances from center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define the constant L
L = 5.0  # Example value for L

# Calculate the output using the given function
myResult = 1 / (1 + distances / L)

print("Original Array:")
print(myArr)
print("\nDistance from Center:")
print(distances)
print("\nResulting Array:")
print(myResult)
