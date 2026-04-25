
import numpy as np

# Create your 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define the parameters
rows, cols = myArr.shape
center_row, center_col = rows / 2, cols / 2
L = 10  # You can change this to your desired value for normalization

# Create coordinate grids
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
d = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Define the function to apply, using broadcasting
def myFunc(d, L):
    return 1 / (1 + d / L)

# Apply the function to the distance array
myResult = myFunc(d, L)

print("Original Array:\n", myArr)
print("Distance from center:\n", d)
print("Result after applying myFunc:\n", myResult)
