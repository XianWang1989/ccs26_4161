
import numpy as np
import scipy.stats

def gaussian_filter(size, sigma):
    # Create a Gaussian filter
    x = np.linspace(-size / 2., size / 2., size)
    y = np.linspace(-size / 2., size / 2., size)
    x, y = np.meshgrid(x, y)  # Create a meshgrid for X and Y coordinates
    gaussian = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    gaussian /= gaussian.sum()  # Normalize the filter
    return gaussian

# Parameters
size = 5
sigma = 1.0

# Get the Gaussian filter
filter = gaussian_filter(size, sigma)
print(filter)
