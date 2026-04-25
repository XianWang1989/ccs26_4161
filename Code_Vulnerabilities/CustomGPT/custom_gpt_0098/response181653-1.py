
import numpy as np
from scipy.stats import multivariate_normal

def gaussian_filter(size, sigma):
    # Create a 2D grid of (x, y) coordinates
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the 2D Gaussian function
    d = np.sqrt(x**2 + y**2)
    g = np.exp(-(d**2) / (2 * sigma**2))

    # Normalize the filter to ensure the sum is 1
    return g / np.sum(g)

# Parameters for the Gaussian filter
filter_size = 5
sigma = 1.0

# Generate the Gaussian filter
gaussian_kernel = gaussian_filter(filter_size, sigma)
print(gaussian_kernel)
