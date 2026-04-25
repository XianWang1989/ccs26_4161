
import numpy as np
import cv2

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array to find the center
height, width = myArr.shape
center = (height / 2, width / 2)

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate distance from the center
distances = np.sqrt((y_indices - center[0]) ** 2 + (x_indices - center[1]) ** 2)

# Define the function with L being the scaling factor
L = 1  # Define your desired scale factor
result = 1 / (1 + distances / L)

# Optionally normalize the image for display using OpenCV
normalized_result = cv2.normalize(result, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

print("Original Array:\n", myArr)
print("Distance from Center:\n", distances)
print("Result:\n", result)
print("Normalized Result for Display:\n", normalized_result)
