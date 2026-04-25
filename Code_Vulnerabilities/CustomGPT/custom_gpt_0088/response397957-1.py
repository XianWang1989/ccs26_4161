
import numpy as np

# Example 2D array (image)
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Dimensions of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows / 2, cols / 2

# Create a grid of row and column indices
Y, X = np.ogrid[:rows, :cols]

# Calculate Euclidean distance from the center
distance = np.sqrt((X - center_col) ** 2 + (Y - center_row) ** 2)

# Function to compute the desired output using the distance
def myFunc(d, L=1):
    return 1 / (1 + d / L)

# Apply the function to the distance array
myResult = myFunc(distance)

print(myResult)
