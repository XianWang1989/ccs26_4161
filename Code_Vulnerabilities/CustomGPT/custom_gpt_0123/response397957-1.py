
import numpy as np

# Sample image array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Define a function to compute the desired value
def compute_value(d, L):
    return 1 / (1 + d / L)

# Calculate the center of the image
center_row, center_col = rows // 2, cols // 2

# Create coordinate grids
y_coords, x_coords = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_coords - center_col) ** 2 + (y_coords - center_row) ** 2)

# Define a parameter L
L = 1.0  # You can adjust this value as needed

# Apply the value function to the distances
myResult = compute_value(distances, L)

print(myResult)
