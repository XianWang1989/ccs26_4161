
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    """Generates a 2D Gaussian filter."""
    # Create a 2D grid of (x,y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]
    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2.0 * sigma**2))
    return g / g.sum()  # Normalize the filter

# Parameters for the Gaussian filter
size = 2  # Half-size of the filter (5x5)
sigma = 1.0  # Standard deviation

# Create the Gaussian filter
gaussian_filter_5x5 = gaussian_filter_2d(size, sigma)

# Print the output
print(gaussian_filter_5x5)
