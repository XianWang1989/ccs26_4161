
import numpy as np

# Sample array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of (row, col) indices
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the distances from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define the L parameter for scaling
L = 5  # Example value

# Define the function that applies the distance calculation
def myFunc(distance):
    return 1 / (1 + distance / L)

# Apply the function using vectorized operations
myResult = myFunc(distances)

# Display the results
print("Original Array:\n", myArr)
print("Distance from Center:\n", distances)
print("Result Array:\n", myResult)
