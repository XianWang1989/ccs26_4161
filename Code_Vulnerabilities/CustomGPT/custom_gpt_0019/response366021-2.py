
import numpy as np
import itertools

# Example lists (shortened for clarity)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a nice "table" of the lists
xy = list(itertools.product(lx, ly))

# Assuming lon and lat are numpy arrays defined earlier
lon = np.array([3.625, 4.625])  # Example data
lat = np.array([41.435, 42.435])  # Example data

b = -1
v = 1

for l in xy:
    b += 1
    idx = np.where(lon == l[0])[0][0]  # Access the first element of tuple
    idy = np.where(lat == l[1])[0][0]  # Access the second element of tuple
    print(f'Index in lon: {idx}, Index in lat: {idy}')
