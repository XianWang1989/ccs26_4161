
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1):
    # Create a 1D Gaussian kernel
    x = np.linspace(-size // 2, size // 2, size)
    g = np.exp(-x**2 / (2 * sigma**2))
    g /= g.sum()  # Normalize the kernel

    # Create a 2D Gaussian filter by outer product
    gaussian_2d = np.outer(g, g)
    return gaussian_2d

# Example usage
filter_size = 5
sigma = 1
gaussian_kernel = gaussian_filter(size=filter_size, sigma=sigma)

print(gaussian_kernel)
