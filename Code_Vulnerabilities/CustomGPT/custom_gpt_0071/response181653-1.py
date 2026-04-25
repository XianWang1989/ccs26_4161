
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    # Create a 2D grid of (x,y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]
    # Calculate the Gaussian filter
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    # Normalize the filter
    return g / g.sum()

# Parameters
filter_size = 2  # Half-width
sigma = 1.0      # Standard deviation

# Create the filter
gaussian_filter = gaussian_filter_2d(filter_size, sigma)
print(gaussian_filter)
