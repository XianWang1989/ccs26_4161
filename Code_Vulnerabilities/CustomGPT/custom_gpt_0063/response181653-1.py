
import numpy as np

def gaussian_filter(size, sigma):
    # Create a grid of (x,y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]

    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2*sigma**2))

    # Normalize the filter
    return g / g.sum()

# Parameters
size = 2  # This will give a 5x5 filter
sigma = 1.0  # Standard deviation

# Generate the Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)

print(gaussian_kernel)
