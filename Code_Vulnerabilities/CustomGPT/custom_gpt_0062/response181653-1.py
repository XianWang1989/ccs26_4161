
import numpy as np

def gaussian_filter(size=5, sigma=1.0):
    """Generates a Gaussian filter."""
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    gaussian = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return gaussian / np.sum(gaussian)  # Normalize the filter

# Create a Gaussian filter
filter_size = 5
sigma_value = 1.0
gaussian_filter_5x5 = gaussian_filter(filter_size, sigma_value)

print(gaussian_filter_5x5)
