
import numpy as np

# Create a sample 2D array (representing an image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define the distance function
def distance_from_center(val, row, col, L):
    # Calculate the center coordinates
    center_row, center_col = myArr.shape[0] // 2, myArr.shape[1] // 2
    # Calculate the Euclidean distance
    d = np.sqrt((row - center_row) ** 2 + (col - center_col) ** 2)
    # Return the computed value based on the distance and L
    return 1 / (1 + d / L)

# Parameters
L = 10  # Arbitrary length scale for the example

# Get the row and column indices
rows, cols = np.indices(myArr.shape)

# Vectorize the distance function
vectorized_func = np.vectorize(distance_from_center)

# Compute results
myResult = vectorized_func(myArr, rows, cols, L)

print(myResult)
