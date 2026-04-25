
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size=5, sigma=1):
    # Create a Gaussian filter
    x = np.linspace(-size // 2 + 1, size // 2, size)
    y = np.linspace(-size // 2 + 1, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate Gaussian value
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    g /= g.sum()  # Normalize the filter

    return g

# Generate a 5x5 Gaussian filter
gaussian_filter_5x5 = gaussian_filter_2d(size=5, sigma=1)
print(gaussian_filter_5x5)
