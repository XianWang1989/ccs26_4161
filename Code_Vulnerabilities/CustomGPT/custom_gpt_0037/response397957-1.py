
import numpy as np

# Create a sample 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Function to compute the distance from the center
def compute_distance(arr):
    rows, cols = arr.shape
    center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

    # Create a grid of coordinates
    y_indices, x_indices = np.indices(arr.shape)

    # Calculate Euclidean distances
    d = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)
    return d

# Function to apply the transformation
def myFunc(val, d, L):
    return 1 / (1 + d / L)

# Main processing
L = 2  # Example constant
distances = compute_distance(myArr)
myResult = myFunc(myArr, distances, L)

print(myResult)
