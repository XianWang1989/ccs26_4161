
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1):
    # Create a 1D Gaussian kernel
    x = np.linspace(-size//2, size//2, size)
    g = np.exp(-0.5 * (x/sigma)**2)
    g = g / g.sum()  # Normalize the kernel

    # Create a 2D Gaussian kernel by outer product
    kernel = np.outer(g, g)
    return kernel

# Example usage
filter_5x5 = gaussian_filter(size=5, sigma=1)
print(filter_5x5)
