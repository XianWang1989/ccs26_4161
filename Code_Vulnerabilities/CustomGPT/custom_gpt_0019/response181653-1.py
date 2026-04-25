
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    """Generate a 2D Gaussian filter."""
    # Create a grid of (x,y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]
    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    # Normalize the filter
    return g / g.sum()

# Parameters
size = 2  # Size of the filter (5x5 means for size=2)
sigma = 1  # Standard deviation

# Generate the Gaussian filter
gaussian_filter_result = gaussian_filter_2d(size, sigma)
print(gaussian_filter_result)
