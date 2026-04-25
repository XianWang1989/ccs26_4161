
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Dimensions of the array
rows, cols = myArr.shape

# Coordinates of the center
center = np.array([rows // 2, cols // 2])

# Generate a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center[1])**2 + (y_indices - center[0])**2)

# Define the function to apply
def myFunc(d, L):
    return 1 / (1 + d / L)

# Example parameter L
L = 5  # Adjust this value as needed

# Apply the function in a vectorized manner
myResult = myFunc(distances, L)

print("Distance array:\n", distances)
print("Resulting array:\n", myResult)
