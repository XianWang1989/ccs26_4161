
import numpy as np
import cv2

# Sample pixel array (2D array representing an image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the image
height, width = myArr.shape

# Calculate the center of the image
center = np.array([height / 2, width / 2])

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
d = np.sqrt((x_indices - center[1])**2 + (y_indices - center[0])**2)

# Define the function to apply to each pixel
L = 1  # A constant for the distance function

def compute_value(d, L):
    return 1 / (1 + d / L)

# Vectorized computation
myResult = compute_value(d, L)

print(myResult)
