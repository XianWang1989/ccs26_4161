
import numpy as np

# Create a sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define the size of the image
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Generate a grid of coordinates for the pixel indices
y_indices, x_indices = np.indices((rows, cols))

# Calculate distances from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define the function to apply based on the distance
L = 10  # You can change this value as needed
def myFunc(d):
    return 1 / (1 + d / L)

# Apply the function to the distances
myResult = myFunc(distances)

print(myResult)
