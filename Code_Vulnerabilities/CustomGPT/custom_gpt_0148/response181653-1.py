
import numpy as np
import scipy.stats

def gaussian_filter(size, sigma):
    """Create a 2D Gaussian filter."""
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)

    # Create a meshgrid
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter
    g_normalized = g / np.sum(g)

    return g_normalized

# Parameters
filter_size = 5
sigma = 1.0

# Generate the Gaussian filter
gaussian_filter_output = gaussian_filter(filter_size, sigma)
print(gaussian_filter_output)
