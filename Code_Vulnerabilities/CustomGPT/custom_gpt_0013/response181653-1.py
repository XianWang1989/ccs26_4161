
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_kernel(size, sigma):
    """Generate a 2D Gaussian kernel."""
    kernel = np.fromfunction(
        lambda x, y: (1 / (2 * np.pi * sigma ** 2)) * 
                      np.exp(-(((x - (size - 1) / 2) ** 2 + 
                                  (y - (size - 1) / 2) ** 2) / (2 * sigma ** 2))),
        (size, size))
    return kernel

# Parameters
size = 5  # 5x5 filter
sigma = 1.0  # Standard deviation

# Create Gaussian filter
gaussian_filter = gaussian_kernel(size, sigma)

# Normalize the filter
gaussian_filter /= np.sum(gaussian_filter)

print(gaussian_filter)
