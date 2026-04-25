
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate Euclidean distances from the center
distances = np.sqrt((y_indices - center_row)**2 + (x_indices - center_col)**2)

# Define your function
def myFunc(distance, L):
    return 1 / (1 + distance / L)

# Apply the function with a specific value for L
L = 5  # Example parameter
myResult = myFunc(distances, L)

print(myResult)
