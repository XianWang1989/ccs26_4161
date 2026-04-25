
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size, sigma):
    # Create a Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size)
    x, y = np.meshgrid(ax, ax)
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g /= g.sum()  # Normalize the filter
    return g

# Parameters
filter_size = 5
sigma = 1.0  # Standard deviation

# Create the filter
gaussian_filter = create_gaussian_filter(filter_size, sigma)
print(gaussian_filter)
