
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size, sigma):
    # Create a grid of (x, y) coordinates
    x = np.linspace(-size // 2 + 1, size // 2, size)
    y = np.linspace(-size // 2 + 1, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian filter
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return g / (2 * np.pi * sigma**2)

# Parameters
filter_size = 5
sigma_value = 1.0

# Generate Gaussian filter
gaussian_filter = create_gaussian_filter(filter_size, sigma_value)
print(gaussian_filter)
