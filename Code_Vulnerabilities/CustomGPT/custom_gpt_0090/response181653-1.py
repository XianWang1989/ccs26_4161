
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    # Create a grid of (x,y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]
    # Compute the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return g / g.sum()

# Parameters
filter_size = 2  # size = 5x5 means size is 2 (for the center pixel)
sigma = 1

# Generate the Gaussian filter
gaussian_filter_5x5 = gaussian_filter_2d(filter_size, sigma)
print(gaussian_filter_5x5)
