
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size, sigma):
    # Create a Gaussian filter of the given size and standard deviation
    filter_size = (size, size)
    # Create a Gaussian function on a grid
    ax = np.linspace(-(size // 2), size // 2, size)
    x, y = np.meshgrid(ax, ax)
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g = g / (2 * np.pi * sigma**2)  # Normalize
    return g

# Parameters
size = 5  # 5x5 filter
sigma = 1.0  # Standard deviation

# Create the filter
gaussian_filter = create_gaussian_filter(size, sigma)
print(gaussian_filter)
