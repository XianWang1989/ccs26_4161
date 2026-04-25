
import numpy as np
from scipy.ndimage import gaussian_filter

# Define the size and sigma
size = 5
sigma = 1.0

# Create a 2D grid of points
x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]

# Calculate the Gaussian filter
g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
g = g / (2 * np.pi * sigma**2)  # Normalize the filter

print(g)
