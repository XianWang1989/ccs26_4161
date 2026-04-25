
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array to find the center
rows, cols = myArr.shape
center_row, center_col = rows // 2, cols // 2

# Create coordinate arrays
x_indices = np.arange(rows).reshape((rows, 1))
y_indices = np.arange(cols).reshape((1, cols))

# Calculate Euclidean distances using broadcasting
distances = np.sqrt((x_indices - center_row)**2 + (y_indices - center_col)**2)

# Define your function
L = 100  # Example scale factor
f = 1 / (1 + distances / L)

print(f)
