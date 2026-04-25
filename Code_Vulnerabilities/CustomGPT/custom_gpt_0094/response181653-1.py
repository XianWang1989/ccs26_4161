
import numpy as np
from scipy.stats import multivariate_normal

def gaussian_filter(size=5, sigma=1):
    # Create a 1D Gaussian kernel
    x = np.linspace(-size//2, size//2, size)
    y = np.linspace(-size//2, size//2, size)
    x, y = np.meshgrid(x, y)

    # Create a 2D Gaussian distribution
    g = multivariate_normal.pdf(np.dstack((x, y)), mean=[0, 0], cov=[[sigma**2, 0], [0, sigma**2]])

    # Normalize the Gaussian filter
    g /= g.sum()
    return g

# Create a 5x5 Gaussian filter
filter_size = 5
sigma_value = 1
gaussian_kernel = gaussian_filter(size=filter_size, sigma=sigma_value)

print(gaussian_kernel)
