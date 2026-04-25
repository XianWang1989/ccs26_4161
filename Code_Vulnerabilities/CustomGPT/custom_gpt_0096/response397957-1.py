
import numpy as np

# Create a sample 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Function to compute the pixel value based on distance
def compute_value(value, distance, L):
    return 1 / (1 + distance / L)

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of row and column indices
y_indices, x_indices = np.ogrid[0:rows, 0:cols]

# Compute Euclidean distance from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Set the value of L (you can adjust this as needed)
L = 5

# Apply the function to all pixel values
myResult = compute_value(myArr, distances, L)

print(myResult)
