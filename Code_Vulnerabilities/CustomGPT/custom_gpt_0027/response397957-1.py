
import numpy as np
import cv2  # If you plan to do more image processing

# Creating a sample 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Define the size of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center_row, center_col = rows // 2, cols // 2

# Create coordinate grids
y_indices, x_indices = np.indices((rows, cols))

# Calculate the distance from the center using Euclidean distance
distance = np.sqrt((y_indices - center_row) ** 2 + (x_indices - center_col) ** 2)

# Define L (a scaling factor)
L = 5  # You can adjust this as needed

# Define your function f(i, j)
def f(d):
    return 1 / (1 + d / L)

# Calculate the result using your function
myResult = f(distance)

print("Resulting array:")
print(myResult)
