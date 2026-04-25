
import numpy as np
import scipy.signal

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    x = np.linspace(-size // 2, size // 2, size)
    g1d = np.exp(-0.5 * (x / sigma) ** 2)
    g1d /= g1d.sum()  # Normalize

    # Create a 2D Gaussian kernel by outer product
    g2d = np.outer(g1d, g1d)
    return g2d

# Parameters
size = 5  # Size of the filter (5x5)
sigma = 1.0  # Standard deviation

gaussian_kernel = gaussian_filter(size, sigma)
print(gaussian_kernel)
