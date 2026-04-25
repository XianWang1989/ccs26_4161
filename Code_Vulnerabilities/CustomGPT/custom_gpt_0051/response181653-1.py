
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    """Create a Gaussian filter."""
    # Create a 1D Gaussian kernel
    ax = np.arange(-size, size + 1)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    g /= g.sum()  # Normalize the filter
    return g

# Parameters
size = 2  # Half width (size = (5-1)/2)
sigma = 1  # Standard deviation

# Generate Gaussian filter
filter_5x5 = gaussian_filter(size, sigma)
print(filter_5x5)
