
import numpy as np
import scipy.stats

def gaussian_filter(size, sigma):
    """Create a Gaussian filter of the specified size and standard deviation."""
    ax = np.arange(-size // 2 + 1., size // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / g.sum()

# Example usage:
size = 5  # Filter size (5x5)
sigma = 1.0  # Standard deviation
gaussian_kernel = gaussian_filter(size, sigma)
print(gaussian_kernel)
