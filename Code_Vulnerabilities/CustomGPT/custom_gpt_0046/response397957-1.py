
import numpy as np

# Example array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of coordinates
x_indices = np.arange(rows).reshape(-1, 1)  # shape (rows, 1)
y_indices = np.arange(cols).reshape(1, -1)  # shape (1, cols)

# Calculate the Euclidean distance from the center
d = np.sqrt((x_indices - center_row) ** 2 + (y_indices - center_col) ** 2)

# Length scale for the distance function
L = 1.0  # Adjust as needed

# Define your function f
def f(i, j):
    return 1 / (1 + d[i, j] / L)

# Apply the function using vectorized operations
myResult = f(*np.indices(myArr.shape))

print("Resulting array:")
print(myResult)
