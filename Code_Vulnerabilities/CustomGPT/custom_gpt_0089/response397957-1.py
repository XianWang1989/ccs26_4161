
import numpy as np

# Example 2D pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get dimensions
rows, cols = myArr.shape

# Calculate center coordinates
center_row, center_col = rows / 2, cols / 2

# Create coordinate grids
x = np.arange(cols)
y = np.arange(rows)
xx, yy = np.meshgrid(x, y)

# Calculate Euclidean distance from the center
distances = np.sqrt((xx - center_col)**2 + (yy - center_row)**2)

# Length L (you can set it as needed)
L = 5  # Example value

# Apply the function for each pixel
myResult = 1 / (1 + distances / L)

print("Distance from center:\n", distances)
print("Result:\n", myResult)
