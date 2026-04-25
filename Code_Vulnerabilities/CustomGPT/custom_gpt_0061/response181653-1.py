
import numpy as np
import scipy.ndimage as ndimage

def gaussian_filter(size, sigma):
    """Generates a Gaussian filter of given size and standard deviation sigma."""
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / g.sum()  # Normalize the filter

# Parameters
size = 5  # Size of the filter (5x5)
sigma = 1  # Standard deviation

# Generate the Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)

print(gaussian_kernel)
