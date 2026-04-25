
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center of the image
center_row = (rows - 1) / 2
center_col = (cols - 1) / 2

# Create a grid of coordinates
Y, X = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
d = np.sqrt((X - center_col) ** 2 + (Y - center_row) ** 2)

# Define the length constant L
L = 2.0  # You can adjust this value as needed

# Apply the function to get the result
myResult = 1 / (1 + d / L)

print(myResult)
