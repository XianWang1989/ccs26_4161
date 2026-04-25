
import numpy as np
from scipy.ndimage import gaussian_filter

# Desired size and sigma
size = 5
sigma = 1.0

# Create a Gaussian filter
def create_gaussian_filter(size, sigma):
    # Create a 2D grid of x and y coordinates
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    gaussian = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    gaussian /= gaussian.sum()  # Normalize the filter

    return gaussian

gaussian_filter = create_gaussian_filter(size, sigma)
print(gaussian_filter)
