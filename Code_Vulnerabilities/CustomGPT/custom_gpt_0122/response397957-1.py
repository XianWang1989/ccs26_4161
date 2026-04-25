
import numpy as np

# Sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define the function to calculate the transformation
def transform_function(val, d, L):
    return 1 / (1 + d / L)

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center of the array
center_row, center_col = rows // 2, cols // 2

# Create grid of coordinates
y_indices, x_indices = np.indices((rows, cols))

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_col)**2 + (y_indices - center_row)**2)

# Define L (e.g., a constant you choose)
L = 5  # You can change this value as needed

# Apply the transformation function using broadcasting
myResult = transform_function(myArr, distances, L)

print(myResult)
