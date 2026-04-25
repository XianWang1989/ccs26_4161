
import numpy as np
from scipy.ndimage import gaussian_filter

# Parameters for the Gaussian filter
size = 5  # size of the kernel (5x5)
sigma = 1.0  # standard deviation

# Create a 5x5 array of zeros
kernel = np.zeros((size, size))

# Create the Gaussian filter
kernel = gaussian_filter(np.zeros((size, size)), sigma=sigma)

# Normalize the kernel to sum to 1
kernel /= np.sum(kernel)

print(kernel)
