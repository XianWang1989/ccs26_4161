
import numpy as np

# Example 2D array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create coordinate grids
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_col)**2 + (y_indices - center_row)**2)

# Define the L parameter (you can adjust it as needed)
L = np.max(distances)  # Example: max distance as L

# Calculate the function for each pixel
result = 1 / (1 + distances / L)

# Display the result
print(result)
