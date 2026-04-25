
import numpy as np

def gaussian_filter(size, sigma):
    # Create a 1D Gaussian kernel
    x = np.arange(-size // 2 + 1, size // 2 + 1)
    gauss = np.exp(-0.5 * (x / sigma)**2)
    gauss /= gauss.sum()  # Normalize

    # Create a 2D filter by outer product
    kernel = np.outer(gauss, gauss)
    return kernel

# Example usage
size = 5  # Size of the filter (5x5)
sigma = 1.0  # Standard deviation
filter_5x5 = gaussian_filter(size, sigma)

print(filter_5x5)
