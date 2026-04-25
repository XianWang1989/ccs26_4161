
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a Gaussian filter
    ax = np.linspace(-(size // 2), size // 2, size)
    x, y = np.meshgrid(ax, ax)
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return g / np.sum(g)  # Normalize the filter

# Parameters
size = 5  # Filter size
sigma = 1.0  # Standard deviation

# Generate the filter
gaussian_kernel = gaussian_filter(size, sigma)
print(gaussian_kernel)
