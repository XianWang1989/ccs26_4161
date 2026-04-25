
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    x = np.linspace(-size // 2, size // 2, size)
    x = np.exp(-0.5 * (x / sigma) ** 2)

    # Create a 2D Gaussian filter by outer product
    g = np.outer(x, x)

    # Normalize the filter
    return g / g.sum()

# Parameters
size = 5
sigma = 1.0

# Generate the Gaussian filter
gaussian = gaussian_filter(size, sigma)
print(gaussian)
