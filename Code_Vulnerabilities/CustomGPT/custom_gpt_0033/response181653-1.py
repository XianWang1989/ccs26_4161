
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a range for the filter
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalize the filter to ensure the sum is 1
    g /= np.sum(g)

    return g

# Parameters
filter_size = 5
sigma = 1.0  # You can adjust sigma as needed

# Generate the filter
gaussian_filter_5x5 = gaussian_filter(filter_size, sigma)
print(gaussian_filter_5x5)
