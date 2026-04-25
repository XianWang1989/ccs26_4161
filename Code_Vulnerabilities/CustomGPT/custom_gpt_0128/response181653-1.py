
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a Gaussian kernel
    ax = np.arange(-size//2 + 1., size//2 + 1.)
    x, y = np.meshgrid(ax, ax)
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return g / g.sum()

# Parameters
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation

# Generate the Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)
print(gaussian_kernel)
