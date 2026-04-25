
import numpy as np

# Create a sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Generate coordinate grids
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center for each pixel
d = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Set your parameter L (you can adjust this value based on your needs)
L = 5

# Apply the function to each pixel
result = 1 / (1 + d / L)

print(result)
