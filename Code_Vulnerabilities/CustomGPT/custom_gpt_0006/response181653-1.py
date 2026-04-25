
import numpy as np
from scipy.ndimage import gaussian_filter

# Parameters
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation

# Create a 2D Gaussian filter
def gaussian_filter_2d(size, sigma):
    # Create an array of the specified size
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)

    # Calculate the Gaussian function
    g = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return g / g.sum()  # Normalize the filter

# Generate the filter
gaussian_filter_5x5 = gaussian_filter_2d(size, sigma)

print(gaussian_filter_5x5)
