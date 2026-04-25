
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    """Create a 2D Gaussian filter."""
    # Create an empty filter
    filter_size = size // 2
    x = np.linspace(-filter_size, filter_size, size)
    y = np.linspace(-filter_size, filter_size, size)
    x, y = np.meshgrid(x, y)

    # Compute the Gaussian
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g /= g.sum()  # Normalize the filter
    return g

# Parameters
size = 5  # Size of the filter (5x5)
sigma = 1  # Standard deviation

# Generate the Gaussian filter
gaussian_filter_5x5 = gaussian_filter_2d(size, sigma)
print(gaussian_filter_5x5)
