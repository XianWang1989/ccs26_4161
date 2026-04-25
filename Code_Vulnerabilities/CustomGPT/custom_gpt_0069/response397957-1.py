
import numpy as np

# Sample pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Image dimensions
rows, cols = myArr.shape
center = (rows - 1) / 2, (cols - 1) / 2  # Center coordinates

# Create grid of coordinates
Y, X = np.ogrid[:rows, :cols]

# Calculate Euclidean distances from the center
d = np.sqrt((X - center[1])**2 + (Y - center[0])**2)

# Define L (a constant for scaling the distance)
L = 2.0  # Adjust this according to your needs

# Apply your function to each pixel
result = 1 / (1 + d / L)

print("Distance from center:\n", d)
print("Resulting processed array:\n", result)
