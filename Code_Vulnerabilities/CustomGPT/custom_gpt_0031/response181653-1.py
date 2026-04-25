
import numpy as np
import scipy.ndimage

def gaussian_filter(size=5, sigma=1.0):
    # Create a 2D Gaussian filter
    x = np.linspace(-size//2 + 1, size//2, size)
    y = np.linspace(-size//2 + 1, size//2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian filter
    gauss = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return gauss / (2 * np.pi * sigma**2)

# Generate a 5x5 Gaussian filter with sigma = 1
filter_size = 5
sigma_value = 1.0
gaussian_filter_result = gaussian_filter(filter_size, sigma_value)

print(gaussian_filter_result)
