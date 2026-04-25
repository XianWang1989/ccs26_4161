
import numpy as np

# Create a sample 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of indices
x, y = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x - center_row) ** 2 + (y - center_col) ** 2)

# Define the function using vectorized operations
L = 1  # You can adjust this value based on your requirements
result = 1 / (1 + distances / L)

print(result)
