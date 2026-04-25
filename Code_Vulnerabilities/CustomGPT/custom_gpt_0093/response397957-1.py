
import numpy as np

# Example pixel array
myArr = np.array([[0, 1, 2],
                  [3, 4, 5]])

# Get the shape of the array
rows, cols = myArr.shape

# Calculate the center coordinates
center = (rows - 1) / 2, (cols - 1) / 2

# Create a grid of coordinates
x_indices = np.arange(rows)
y_indices = np.arange(cols)
x_grid, y_grid = np.meshgrid(x_indices, y_indices, indexing='ij')

# Calculate the Euclidean distance from the center
distances = np.sqrt((x_grid - center[0])**2 + (y_grid - center[1])**2)

# Set a length scale L (you can adjust this value)
L = 2.0

# Calculate the final result using your specified function
myResult = 1 / (1 + distances / L)

# Display the results
print("Distances from center:")
print(distances)
print("Final result:")
print(myResult)
