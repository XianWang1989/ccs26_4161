
import numpy as np

# Example array (2D pixel array)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Dimensions of the array
rows, cols = myArr.shape

# Define the center point
center_row, center_col = rows / 2, cols / 2

# Function to compute the desired value based on distance
def compute_function(i, j, L):
    # Calculate Euclidean distance from the center
    d = np.sqrt((i - center_row) ** 2 + (j - center_col) ** 2)
    return 1 / (1 + d / L)

# Prepare grid of indices
Y, X = np.indices(myArr.shape)

# Define L (you can set L to any positive value you need)
L = 10

# Vectorized computation
myResult = compute_function(Y, X, L)

# Print the result
print(myResult)
