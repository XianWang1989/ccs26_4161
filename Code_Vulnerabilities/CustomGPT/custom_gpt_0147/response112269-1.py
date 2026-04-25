
import numpy as np
import matplotlib.pyplot as plt

# Sample data: a list of lines represented by their endpoints and corresponding probabilities
lines = [
    ((0, 0), (10, 10), 0.8),  # Line from (0,0) to (10,10) with probability 0.8
    ((0, 10), (10, 0), 0.5),  # Line from (0,10) to (10,0) with probability 0.5
    # Add more lines as necessary...
]

# Create a grid for the density
grid_size = (100, 100)
grid = np.zeros(grid_size)

# Define limits for x and y axis
x_limits = (0, 10)
y_limits = (0, 10)

# Create a meshgrid for x and y
x = np.linspace(x_limits[0], x_limits[1], grid_size[0])
y = np.linspace(y_limits[0], y_limits[1], grid_size[1])
X, Y = np.meshgrid(x, y)

# Convert endpoints into grid indices
for (start, end, prob) in lines:
    # Create line between start and end
    line_x = np.linspace(start[0], end[0], 100)
    line_y = np.linspace(start[1], end[1], 100)

    # Update grid with intensity based on the probability
    for i in range(len(line_x)):
        xi = np.clip(np.searchsorted(x, line_x[i]), 0, grid_size[0] - 1)
        yi = np.clip(np.searchsorted(y, line_y[i]), 0, grid_size[1] - 1)
        grid[yi, xi] += prob  # accumulate probability

# Normalize the grid to be between 0-1
grid = np.clip(grid / grid.max(), 0, 1)

# Plotting the density plot
plt.imshow(grid, extent=[*x_limits, *y_limits], origin='lower', cmap='hot', alpha=0.5)
plt.colorbar(label='Intensity')
plt.title('2D Density Plot with Distinct Lines')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid()
plt.show()
