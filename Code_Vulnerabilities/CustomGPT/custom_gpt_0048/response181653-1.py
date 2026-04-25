
import numpy as np
from scipy.ndimage import gaussian_filter

# Define parameters
size = 5  # size of the filter
sigma = 1.0  # standard deviation

# Create a grid of (x, y) coordinates
x, y = np.mgrid[-(size//2):(size//2)+1, -(size//2):(size//2)+1]

# Calculate Gaussian filter
g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
g /= (2 * np.pi * sigma**2)  # normalize to ensure the sum is 1

print(g)
