
import numpy as np
import cv2

# Create a sample 2D numpy pixel array (for example, an image of shape 3x3)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = rows / 2, cols / 2

# Create a grid of row and column indices
row_indices, col_indices = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

# Calculate the Euclidean distance from the center
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define your function to get the desired output
L = 5  # You can set this to whatever constant you'd like
def my_func(d):
    return 1 / (1 + d / L)

# Apply the function to the distances
myResult = my_func(distances)

print("Input Array:\n", myArr)
print("Distances from Center:\n", distances)
print("Computed Result:\n", myResult)
