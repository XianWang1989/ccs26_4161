
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    # Create a 2D Gaussian filter
    ax = np.linspace(-(size // 2), size // 2, size)
    x, y = np.meshgrid(ax, ax)
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return g / g.sum()  # Normalize the filter

# Parameters
filter_size = 5
sigma = 1.0  # Standard deviation

# Create the Gaussian filter
gaussian_filter_5x5 = gaussian_filter_2d(filter_size, sigma)
print(gaussian_filter_5x5)
