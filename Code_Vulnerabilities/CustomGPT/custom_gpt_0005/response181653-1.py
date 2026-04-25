
import numpy as np
from scipy.ndimage import gaussian_filter

def gaussian_filter_2d(size, sigma):
    # Create a 2D Gaussian filter
    gauss = np.zeros((size, size))
    for x in range(size):
        for y in range(size):
            gauss[x, y] = (1 / (2 * np.pi * sigma**2)) * np.exp(-((x - (size-1)/2)**2 + (y - (size-1)/2)**2) / (2 * sigma**2))
    return gauss

size = 5
sigma = 1.0
filter_5x5 = gaussian_filter_2d(size, sigma)

print(filter_5x5)
