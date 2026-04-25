
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    """Create a 2D Gaussian filter."""
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g /= (2 * np.pi * sigma**2)  # Normalize
    return g

# Parameters
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation

# Create the filter
gaussian_filter = gaussian_filter_2d(size, sigma)
print(gaussian_filter)
