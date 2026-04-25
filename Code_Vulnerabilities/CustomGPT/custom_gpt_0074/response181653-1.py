
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1.0):
    # Create a 1D Gaussian kernel
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    gaussian = (1 / (2 * np.pi * sigma ** 2)) * np.exp(-(xx ** 2 + yy ** 2) / (2 * sigma ** 2))

    # Normalize the Gaussian filter to ensure the sum is 1
    return gaussian / np.sum(gaussian)

# Example usage
size = 5
sigma = 1.0
filter_matrix = gaussian_filter(size, sigma)
print(filter_matrix)
