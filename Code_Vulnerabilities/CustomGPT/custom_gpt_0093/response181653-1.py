
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size=5, sigma=1):
    # Create a 2D grid of (x, y) coordinates
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)

    # Calculate the 2D Gaussian function
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))

    # Normalize the kernel
    kernel /= np.sum(kernel)

    return kernel

# Generate a 5x5 Gaussian filter with sigma=1
gaussian_kernel = gaussian_filter_2d(size=5, sigma=1)
print(gaussian_kernel)
