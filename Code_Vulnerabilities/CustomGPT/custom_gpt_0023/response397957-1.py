
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Image dimensions
rows, cols = myArr.shape

# Find the center of the image
center_x, center_y = (cols - 1) / 2, (rows - 1) / 2

# Create a grid of coordinates
x = np.arange(cols)
y = np.arange(rows)
x, y = np.meshgrid(x, y)

# Calculate the Euclidean distance from the center
d = np.sqrt((x - center_x)**2 + (y - center_y)**2)

# Define the L constant (modify according to your needs)
L = 10  # Example value

# Calculate the final result based on the distance
myResult = 1 / (1 + d / L)

print(myResult)
