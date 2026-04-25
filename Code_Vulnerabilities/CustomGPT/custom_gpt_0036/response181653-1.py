
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    """Generates a Gaussian filter."""
    # Create a grid of (x,y) coordinates
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter
    return g / np.sum(g)

# Define the size and standard deviation (sigma)
size = 5
sigma = 1.0

# Generate the Gaussian filter
gaussian_filter_result = gaussian_filter(size, sigma)
print(gaussian_filter_result)
