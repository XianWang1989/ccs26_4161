import numpy as np

# Example image size (2x3)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Image dimensions
rows, cols = myArr.shape

# Center coordinates
center_row, center_col = rows / 2, cols / 2

# Generate row and column indices
y_indices, x_indices = np.indices((rows, cols))

# Compute Euclidean distance from the center
distances = np.sqrt((y_indices - center_row)**2 + (x_indices - center_col)**2)

# Example constant L
L = 5.0

# Apply the function to each pixel
result = 1 / (1 + distances / L)

print("Distance from center:")
print(distances)

print("\nResult after applying function:")
print(result)
