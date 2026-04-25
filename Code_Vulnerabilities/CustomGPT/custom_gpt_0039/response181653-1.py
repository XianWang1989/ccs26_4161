
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    x = np.linspace(-size // 2, size // 2, size)
    g = np.exp(-0.5 * (x / sigma) ** 2)
    g /= g.sum()  # Normalize the kernel

    # Create a 2D Gaussian kernel
    g2d = np.outer(g, g)
    return g2d

# Parameters
filter_size = 5
sigma = 1.0

# Generate the Gaussian filter
gaussian_kernel = gaussian_filter(filter_size, sigma)

print(gaussian_kernel)
