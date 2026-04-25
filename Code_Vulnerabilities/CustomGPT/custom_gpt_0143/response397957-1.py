
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define dimensions
rows, cols = myArr.shape
center_row, center_col = rows // 2, cols // 2

# Create a grid of row and column indices
y_indices, x_indices = np.indices(myArr.shape)

# Calculate Euclidean distance from the center
d = np.sqrt((y_indices - center_row)**2 + (x_indices - center_col)**2)

# Constant L (for normalization)
L = 5  # Example value

# Function to calculate the result
result = 1 / (1 + d / L)

# Display the result
print("Resulting array based on distance from center:")
print(result)
