
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    # Generate a 2D grid of (x, y) coordinates
    x = np.linspace(-size // 2 + 1, size // 2, size)
    y = np.linspace(-size // 2 + 1, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    gaussian = np.exp(-(x**2 + y**2) / (2 * sigma ** 2))
    gaussian /= np.sum(gaussian)  # Normalize the filter

    return gaussian

# Parameters
size = 5  # Size of the filter (5x5)
sigma = 1.0  # Standard deviation for the Gaussian

# Create the Gaussian filter
gaussian_filter_result = gaussian_filter_2d(size, sigma)
print(gaussian_filter_result)
