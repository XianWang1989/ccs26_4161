
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of row and column indices
row_indices = np.arange(rows)[:, np.newaxis]  # Column vector
col_indices = np.arange(cols)                  # Row vector

# Calculate the Euclidean distance from the center
distances = np.sqrt((row_indices - center_row)**2 + (col_indices - center_col)**2)

# Define your function that uses the distance
def myFunc(val, distance, L):
    return 1 / (1 + distance / L)

# Set a value for L
L = 10  # you can change this according to your needs

# Apply the function element-wise
myResult = myFunc(myArr, distances, L)

print("Original Array:")
print(myArr)
print("\nDistance from center:")
print(distances)
print("\nResult Array:")
print(myResult)
