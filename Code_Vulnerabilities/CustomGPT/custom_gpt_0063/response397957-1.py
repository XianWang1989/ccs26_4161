
import numpy as np

# Define the image array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2
L = 1.0  # Scale factor (you can change this)

# Generate row and column indices
y_indices, x_indices = np.indices(myArr.shape)

# Calculate Euclidean distance from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Apply the function to compute the result
myResult = 1 / (1 + distances / L)

print("Original Array:")
print(myArr)
print("Distance Result Array:")
print(myResult)
