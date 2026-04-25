
import numpy as np

# Create a sample image array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array to find the center
rows, cols = myArr.shape
center_row, center_col = rows / 2, cols / 2

# Create coordinate grids
x = np.arange(rows).reshape(rows, 1)  # (rows, 1)
y = np.arange(cols).reshape(1, cols)  # (1, cols)

# Calculate the Euclidean distance from the center
d = np.sqrt((x - center_row) ** 2 + (y - center_col) ** 2)

# Define the function using the distance
L = 2  # Example value for L
result = 1 / (1 + d / L)

print("Original Array:")
print(myArr)
print("Distance Transform Result:")
print(result)
