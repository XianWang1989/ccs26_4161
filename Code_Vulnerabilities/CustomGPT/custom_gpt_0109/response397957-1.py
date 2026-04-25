
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get array shape
rows, cols = myArr.shape

# Calculate the center of the image
center_row, center_col = rows / 2, cols / 2

# Create coordinate grids
y_indices, x_indices = np.indices((rows, cols))

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Define your function
L = 1.0  # Define L as needed
def my_func(dist):
    return 1 / (1 + dist / L)

# Apply the function to distances
my_result = my_func(distances)

print("Pixel Array:\n", myArr)
print("Distance Result:\n", my_result)
