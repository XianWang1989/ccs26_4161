
import numpy as np

# Example pixel array (2D image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Calculate the center of the array
height, width = myArr.shape
center_row, center_col = height // 2, width // 2
L = np.sqrt(center_row**2 + center_col**2)  # This can be adjusted as needed

# Create a grid of coordinates that corresponds to each pixel
row_indices, col_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from each pixel to the center
d = np.sqrt((row_indices - center_row)**2 + (col_indices - center_col)**2)

# Define the function that normalizes based on the distance
def myFunc(d, L):
    return 1 / (1 + d / L)

# Apply the function to the distance array
myResult = myFunc(d, L)

print("Original Array:")
print(myArr)
print("\nDistance from Center:")
print(d)
print("\nResult Array:")
print(myResult)
