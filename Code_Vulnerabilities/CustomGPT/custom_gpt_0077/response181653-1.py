
import numpy as np
import scipy.ndimage

def gaussian_filter(size: int, sigma: float):
    """Create a Gaussian filter using a specified size and sigma."""
    # Create a grid of (x,y) coordinates
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g /= g.sum()  # Normalize the filter
    return g

# Parameters
filter_size = 5
sigma = 1.0

# Create the filter
gaussian_filter_5x5 = gaussian_filter(filter_size, sigma)
print(gaussian_filter_5x5)
