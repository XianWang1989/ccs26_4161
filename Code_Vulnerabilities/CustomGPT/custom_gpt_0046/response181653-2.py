
import numpy as np

def gaussian_filter(size, sigma):
    filter_size = (size, size)
    g = np.zeros(filter_size)
    center = size // 2

    for x in range(size):
        for y in range(size):
            g[x, y] = (1/(2 * np.pi * sigma**2)) * np.exp(-((x - center) ** 2 + (y - center) ** 2) / (2 * sigma ** 2))

    return g / np.sum(g)

# Create a Gaussian filter
filter_5x5 = gaussian_filter(5, 1)
print(filter_5x5)
