
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array to find the center
rows, cols = myArr.shape
center = np.array([rows / 2, cols / 2])

# Create coordinate grid for the pixel locations
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center[1])**2 + (y_indices - center[0])**2)

# Define the function using the distance
def myFunc(d, L=1):
    return 1 / (1 + d / L)

# Apply the function to the distances
myResult = myFunc(distances)

print("Pixel Array:")
print(myArr)
print("\nDistances from Center:")
print(distances)
print("\nResulting Output:")
print(myResult)
