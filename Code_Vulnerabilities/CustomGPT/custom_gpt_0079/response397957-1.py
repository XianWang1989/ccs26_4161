
import numpy as np

# Define the 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of coordinates for the pixels
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_col)**2 + (y_indices - center_row)**2)

# Define the parameter L
L = np.max(distances)  # Example: normalize by maximum distance

# Apply the distance function
result = 1 / (1 + distances / L)

print("Input Array:")
print(myArr)
print("Distances from Center:")
print(distances)
print("Resulting Array:")
print(result)
