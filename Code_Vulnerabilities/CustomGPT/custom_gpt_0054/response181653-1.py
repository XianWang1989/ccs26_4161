
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    # Create a grid of (x, y) coordinates
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g /= g.sum()  # Normalize the filter

    return g

# Example usage
size = 5
sigma = 1.0
filter = gaussian_filter_2d(size, sigma)
print(filter)
