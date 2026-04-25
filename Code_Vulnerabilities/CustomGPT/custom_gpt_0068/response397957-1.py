
import numpy as np

# Sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2
L = 5  # Example constant L

# Get indices of each pixel
y_indices, x_indices = np.indices(myArr.shape)

# Calculate Euclidean distance from the center
d = np.sqrt((x_indices - center_col)**2 + (y_indices - center_row)**2)

# Apply your function f(i, j) = 1/(1 + d(i, j)/L)
result = 1 / (1 + d / L)

print("Original Array:")
print(myArr)
print("Distance Result:")
print(result)
