
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size, sigma):
    # Create a 2D Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size)
    x, y = np.meshgrid(ax, ax)
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return g / g.sum()  # Normalize the kernel

# Example usage
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation
gaussian_kernel = create_gaussian_filter(size, sigma)

print(gaussian_kernel)
