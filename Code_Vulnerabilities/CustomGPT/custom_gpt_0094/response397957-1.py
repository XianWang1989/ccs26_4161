
import numpy as np

# Create a sample NumPy array (representing an image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center for each pixel
distances = np.sqrt((x_indices - center_col) ** 2 + (y_indices - center_row) ** 2)

# Define the function that uses the distances
L = 5  # Example length parameter
result = 1 / (1 + distances / L)

# Display the resulting array
print(result)
