
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1):
    # Ensure size is odd
    if size % 2 == 0:
        size += 1
    # Create a 1D Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size)
    # Create a 2D Gaussian filter
    x, y = np.meshgrid(ax, ax)
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return g / g.sum()  # Normalize the filter

# Example usage
filter_size = 5
sigma_value = 1
gaussian_filter_matrix = gaussian_filter(filter_size, sigma_value)

print(gaussian_filter_matrix)
