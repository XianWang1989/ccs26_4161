
import numpy as np

# Sample 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape
center_row, center_col = rows // 2, cols // 2

# Create a meshgrid of coordinates
x_indices, y_indices = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')

# Calculate distances from the center
d = np.sqrt((x_indices - center_row)**2 + (y_indices - center_col)**2)

# Define the function
L = 10  # A constant for scaling
f = 1 / (1 + d / L)

# Apply to the pixel values if needed (e.g., multiplying with myArr)
myResult = f * myArr

print("Euclidean distances:\n", d)
print("Resulting pixel values:\n", myResult)
