
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    """Create a Gaussian filter."""
    # Create a 2D grid of (x, y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter to sum to 1
    return g / g.sum()

# Parameters
filter_size = 2  # size of the filter (5x5 means size=2)
sigma = 1.0      # standard deviation

# Generate the Gaussian filter
gaussian_filter_output = gaussian_filter(filter_size, sigma)

print(gaussian_filter_output)
