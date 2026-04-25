
import numpy as np

# Sample 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row = rows // 2
center_col = cols // 2

# Create a grid of row and column indices
y_indices, x_indices = np.indices((rows, cols))

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_indices - center_col)**2 + (y_indices - center_row)**2)

# Define the length parameter L
L = 5  # Adjust as needed

# Apply the function to calculate the result
myResult = 1 / (1 + distances / L)

# Output the result
print(myResult)
