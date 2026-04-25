
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 2D grid of (x,y) coordinates
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g /= (2 * np.pi * sigma**2)

    return g

# Parameters
size = 5  # Size of the filter
sigma = 1.0  # Standard deviation

# Generate the Gaussian filter
filter = gaussian_filter(size, sigma)
print(filter)
