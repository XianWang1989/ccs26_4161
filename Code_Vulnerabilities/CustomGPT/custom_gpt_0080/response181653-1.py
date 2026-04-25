
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    """Generates a Gaussian filter."""
    # Create a 1D Gaussian kernel
    x = np.arange(-size//2 + 1, size//2 + 1)
    g = np.exp(-(x**2 / (2 * sigma**2)))
    g = g / g.sum()  # Normalize
    # Create 2D Gaussian filter by outer product
    gaussian_2d = np.outer(g, g)
    return gaussian_2d

# Parameters
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation

# Generate the Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)

print(gaussian_kernel)
