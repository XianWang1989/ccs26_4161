
import numpy as np
from scipy.ndimage import gaussian_filter

# Parameters
size = 5  # Size of the filter
sigma = 1  # Standard deviation for Gaussian

# Create a uniform array
image = np.zeros((size, size))

# Apply the Gaussian filter to an array (to create the distribution)
gaussian_kernel = gaussian_filter(image, sigma=sigma)

print(gaussian_kernel)
