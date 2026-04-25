
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create coordinate grid for the array
y_indices, x_indices = np.indices(myArr.shape)

# Calculate Euclidean distance from the center
distances = np.sqrt((x_indices - center_col)**2 + (y_indices - center_row)**2)

# Define the constant L
L = 5  # Example constant value

# Apply the function
result = 1 / (1 + distances / L)

# Print the results
print("Original Array:\n", myArr)
print("Distance from Center:\n", distances)
print("Result:\n", result)
