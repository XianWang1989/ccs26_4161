
import numpy as np
import cv2

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the center coordinates
center = (myArr.shape[0] // 2, myArr.shape[1] // 2)

# Create a grid of coordinates
x, y = np.indices(myArr.shape)

# Calculate the distances from the center
d = np.sqrt((x - center[0])**2 + (y - center[1])**2)

# Define the function to compute the desired operation
L = 1  # You can adjust L as needed
result = 1 / (1 + d / L)

# Show the result
print(result)
