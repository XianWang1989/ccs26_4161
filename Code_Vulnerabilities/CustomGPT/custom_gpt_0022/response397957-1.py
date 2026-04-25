
import numpy as np
import cv2

# Create a sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_x, center_y = cols / 2, rows / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_x)**2 + (y_indices - center_y)**2)

# Given L value
L = 5  # Adjust this as needed

# Function to compute the desired output
def myFunc(distance):
    return 1 / (1 + distance / L)

# Apply the function using vectorized operations
myResult = myFunc(distances)

print(myResult)
