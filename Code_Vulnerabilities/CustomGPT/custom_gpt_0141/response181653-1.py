
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Generate a 1D Gaussian kernel
    x = np.linspace(-size // 2, size // 2, size)
    gauss = np.exp(-0.5 * (x ** 2) / (sigma ** 2))

    # Normalize the kernel
    gauss = gauss / np.sum(gauss)

    # Create a 2D Gaussian filter by outer product
    gaussian_2d = np.outer(gauss, gauss)

    return gaussian_2d

# Parameters for the Gaussian filter
size = 5  # Size of the filter (5x5)
sigma = 1.0  # Standard deviation

# Generate the Gaussian filter
filter_5x5 = gaussian_filter(size, sigma)

print(filter_5x5)
