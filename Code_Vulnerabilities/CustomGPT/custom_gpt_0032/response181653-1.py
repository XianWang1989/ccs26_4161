
import numpy as np

def gaussian_filter(size, sigma):
    # Create a grid of (x,y) coordinates
    x, y = np.mgrid[-size:size+1, -size:size+1]
    # Calculate the Gaussian function
    g = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return g / g.sum()  # Normalize the filter

# Parameters
filter_size = 2  # `f_wid` in MATLAB
sigma = 1.0      # Standard deviation

# Create the Gaussian filter
gaussian_kernel = gaussian_filter(filter_size, sigma)
print(gaussian_kernel)
