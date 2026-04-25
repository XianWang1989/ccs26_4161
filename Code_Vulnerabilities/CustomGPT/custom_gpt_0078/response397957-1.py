
import numpy as np
import cv2

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Dimensions of the array
rows, cols = myArr.shape
center = np.array([rows / 2, cols / 2])

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((y_indices - center[0])**2 + (x_indices - center[1])**2)

# Define the L value
L = 5  # Adjust as needed

# Apply the function to calculate the result based on distance
result = 1 / (1 + distances / L)

print(result)
