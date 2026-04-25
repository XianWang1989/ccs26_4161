
import numpy as np

# Create a sample 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Define the center coordinates
center_row, center_col = rows // 2, cols // 2

# Create a grid of (row, col) coordinates
y_indices, x_indices = np.indices(myArr.shape)

# Calculate the Euclidean distance from the center
distances = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define the parameter L
L = 10  # You can adjust this value as needed

# Apply the function to compute the result
result = 1 / (1 + distances / L)

print("Original Array:")
print(myArr)
print("\nCalculated Result:")
print(result)
