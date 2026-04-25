
import numpy as np
from scipy.ndimage import gaussian_filter

# Parameters
size = 5  # size of the filter
sigma = 1.0  # standard deviation

# Create a Gaussian filter
def gaussian_kernel(size, sigma):
    """Generates a Gaussian kernel."""
    ax = np.arange(-size // 2 + 1., size // 2 + 1.)
    x, y = np.meshgrid(ax, ax)
    kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return kernel / np.sum(kernel)

# Generate the kernel
gaussian_filter = gaussian_kernel(size, sigma)

print(gaussian_filter)
