
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    x = np.linspace(-size // 2, size // 2, size)
    g = np.exp(-(x**2) / (2 * sigma**2))

    # Normalize the kernel
    g /= g.sum()

    # Create a 2D Gaussian filter by outer product
    gaussian_filter_2d = np.outer(g, g)
    return gaussian_filter_2d

# Parameters
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation

# Create Gaussian filter
filter_2d = gaussian_filter(size, sigma)
print(filter_2d)
