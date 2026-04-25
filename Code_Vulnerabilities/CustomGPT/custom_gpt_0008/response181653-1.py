
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    # Create a 2D Gaussian filter
    # Generate the grid of (x,y) coordinates
    ax = np.arange(-size, size + 1, 1)
    x, y = np.meshgrid(ax, ax)

    # Calculate the 2D Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g /= g.sum()  # Normalize the filter

    return g

# Example usage
size = 2  # Filter size (5x5)
sigma = 1.0  # Standard deviation
gaussian_filter = gaussian_filter_2d(size, sigma)
print(gaussian_filter)
