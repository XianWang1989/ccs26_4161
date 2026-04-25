
import numpy as np

def gaussian_filter(size, sigma):
    """Create a Gaussian filter."""
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / np.sum(g)  # Normalize the Gaussian filter

# Parameters
filter_size = 5
sigma = 1.0

# Create filter
gaussian_filter_output = gaussian_filter(filter_size, sigma)
print(gaussian_filter_output)
