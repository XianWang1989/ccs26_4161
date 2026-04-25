
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a range from -size to size
    x = np.linspace(-size//2, size//2, size)
    y = np.linspace(-size//2, size//2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the Gaussian filter
    g /= np.sum(g)
    return g

# Parameters for the Gaussian filter
filter_size = 5  # size of the filter (5x5)
sigma = 1.0      # standard deviation

# Generate the Gaussian filter
gaussian_filter_5x5 = gaussian_filter(filter_size, sigma)
print(gaussian_filter_5x5)
