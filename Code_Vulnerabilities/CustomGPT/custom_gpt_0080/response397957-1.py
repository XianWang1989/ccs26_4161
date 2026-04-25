
import numpy as np
import cv2

# Sample array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Define your function to apply the distance calculation
def my_func(d, L):
    return 1 / (1 + d / L)

# Set a distance scale L
L = 1.0  # Adjust as necessary

# Apply the function using vectorized operations
myResult = my_func(distances, L)

print("Distances:\n", distances)
print("Result:\n", myResult)
