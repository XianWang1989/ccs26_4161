
import numpy as np

# Create a sample 2D numpy array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array to find the center
rows, cols = myArr.shape
center_row, center_col = rows / 2, cols / 2

# Create coordinate arrays for the pixel positions
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center for each pixel
d = np.sqrt((y_indices - center_row)**2 + (x_indices - center_col)**2)

# Specify L (a constant)
L = 3.0  # You can adjust this value

# Compute the function based on the distance
def myFunc(distance, L):
    return 1 / (1 + distance / L)

# Apply the function vectorized over the distance array
myResult = myFunc(d, L)

print("Original Array:\n", myArr)
print("Distance from Center:\n", d)
print("Result after applying function:\n", myResult)
