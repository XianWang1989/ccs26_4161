
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    """Create a Gaussian filter."""
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / g.sum()

# Parameters
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation of the Gaussian

# Create the Gaussian filter
filter_ = gaussian_filter(size, sigma)
print(filter_)
