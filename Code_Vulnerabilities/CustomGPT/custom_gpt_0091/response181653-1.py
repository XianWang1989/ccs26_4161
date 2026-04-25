
import numpy as np
from scipy.ndimage import gaussian_filter

def create_gaussian_filter(size, sigma):
    # Create a 2D Gaussian filter
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Compute the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter
    return g / g.sum()

# Parameters
size = 5  # Size of the filter (5x5)
sigma = 1.0  # Standard deviation

# Create the filter
gaussian_filter = create_gaussian_filter(size, sigma)
print(gaussian_filter)
