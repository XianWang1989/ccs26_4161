
import numpy as np

# Define the size of the array (image dimensions)
height, width = 5, 5  # Example dimensions

# Create a 2D array (image)
myArr = np.arange(height * width).reshape((height, width))

# Calculate the coordinates of the center
center_x, center_y = width / 2, height / 2

# Create arrays of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from each pixel to the center
distances = np.sqrt((x_indices - center_x) ** 2 + (y_indices - center_y) ** 2)

# Define the function to apply based on distance
L = 10  # Define L for scaling
def myFunc(d):
    return 1 / (1 + d / L)

# Apply the function to the distances
myResult = myFunc(distances)

# Show the original array and resulting array
print("Original Array:")
print(myArr)
print("\nResulting Array:")
print(myResult)
