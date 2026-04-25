
import numpy as np
import scipy.ndimage

def gaussian_filter(size, sigma):
    # Create a grid of (x,y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]
    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2*sigma**2))
    # Normalize the filter to ensure the sum of coefficients is 1
    return g / g.sum()

# Parameters
size = 2  # radius
sigma = 1.0  # standard deviation

# Create the Gaussian filter
gaussian_kernel = gaussian_filter(size, sigma)
print(gaussian_kernel)
