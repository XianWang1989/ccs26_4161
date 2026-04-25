
import numpy as np

# Example 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the dimensions of the array
rows, cols = myArr.shape

# Define the center coordinates
center_row, center_col = (rows - 1) / 2, (cols - 1) / 2

# Create a meshgrid of coordinates
y, x = np.indices((rows, cols))

# Calculate the Euclidean distance from the center
d = np.sqrt((x - center_col) ** 2 + (y - center_row) ** 2)

# Define the function to apply
L = 1.0  # Example constant for distance scaling
def myFunc(distance):
    return 1 / (1 + distance / L)

# Apply the function vectorized on the distance array
myResult = myFunc(d)

print("Original Array:\n", myArr)
print("Resulting Array:\n", myResult)
