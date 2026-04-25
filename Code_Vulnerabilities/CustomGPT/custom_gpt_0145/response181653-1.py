
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    gauss_1d = np.linspace(-size // 2 + 1, size // 2, size)
    gauss_1d = np.exp(-0.5 * (gauss_1d / sigma) ** 2)
    gauss_1d /= gauss_1d.sum()  # Normalize

    # Create a 2D Gaussian kernel by outer product of the 1D kernel
    gauss_2d = np.outer(gauss_1d, gauss_1d)
    return gauss_2d

# Example usage
size = 5
sigma = 1.0
filter_2d = gaussian_filter(size, sigma)
print(filter_2d)
