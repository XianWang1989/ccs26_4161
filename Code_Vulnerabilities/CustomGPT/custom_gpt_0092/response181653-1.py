
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    """Creates a 2D Gaussian filter."""
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / g.sum()  # Normalize the filter

# Parameters
size = 5  # Size of the filter (5x5)
sigma = 1.0  # Standard deviation

# Create the Gaussian filter
gaussian_filter = gaussian_filter_2d(size, sigma)
print(gaussian_filter)
