
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    x = np.linspace(-size // 2, size // 2, size)
    g = np.exp(-0.5 * (x / sigma) ** 2)
    g /= g.sum()  # Normalize the kernel

    # Create a 2D filter by outer product
    gaussian_filter_2d = np.outer(g, g)
    return gaussian_filter_2d

# Example usage
size = 5   # Filter size (5x5)
sigma = 1  # Standard deviation
filter_2d = gaussian_filter(size, sigma)
print(filter_2d)
