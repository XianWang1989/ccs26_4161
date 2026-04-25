
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    """Generates a Gaussian filter."""
    # Create a 2D grid of (x,y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter
    return g / g.sum()

# Define parameters
filter_size = 2  # Corresponds to 5x5 filter (size is 2, so 5 = 2*2 + 1)
sigma = 1.0

# Generate the filter
gaussian_filter_5x5 = gaussian_filter(filter_size, sigma)
print(gaussian_filter_5x5)
