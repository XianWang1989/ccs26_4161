
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a grid of (x,y) coordinates
    x = np.linspace(-size//2, size//2, size)
    y = np.linspace(-size//2, size//2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the 2D Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g /= g.sum()  # Normalize to ensure the sum is 1

    return g

# Parameters
filter_size = 5
sigma = 1.0

# Generate the filter
gaussian = gaussian_filter(filter_size, sigma)
print(gaussian)
