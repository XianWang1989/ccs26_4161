
import numpy as np

# Create a sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of row and column indices
row_indices, col_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center for each pixel
distance_from_center = np.sqrt((row_indices - center_row) ** 2 + (col_indices - center_col) ** 2)

# Define your function based on distance
L = 1  # Adjust as needed
def my_func(d):
    return 1 / (1 + d / L)

# Apply the function to the distance array
my_result = my_func(distance_from_center)

print("Original Array:\n", myArr)
print("Distance from Center:\n", distance_from_center)
print("Result after applying function:\n", my_result)
