
import numpy as np

# Define your pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a meshgrid to get the pixel coordinates
col_indices, row_indices = np.meshgrid(np.arange(cols), np.arange(rows))

# Calculate the Euclidean distance from the center for each pixel
distances = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define the function to apply
def myFunc(d, L):
    return 1 / (1 + d / L)

# Set a value for L
L = 1  # You can change this value as per your logic

# Apply the function using the calculated distances
myResult = myFunc(distances, L)

print(myResult)
