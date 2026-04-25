
import numpy as np

def gaussian_filter(size, sigma):
    """Create a Gaussian filter."""
    ax = np.arange(-size // 2 + 1., size // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-0.5 * (np.square(xx) + np.square(yy)) / np.square(sigma))
    return g / np.sum(g)

# Parameters
size = 5  # Filter size
sigma = 1.0  # Standard deviation

# Generate Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)
print(gaussian_kernel)
