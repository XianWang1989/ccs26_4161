
import numpy as np
import itertools

# Sample lists
lx = [3.625, 4.625]  # Example values
ly = [41.435, 42.435]  # Example values

# Create Cartesian product
xy = list(itertools.product(lx, ly))

# Assuming lon and lat are defined earlier in your code
lon = np.array([3.625, 4.625, 5.625])  # Dummy example
lat = np.array([41.435, 42.435, 43.435])  # Dummy example

for l in xy:
    # Unpack the tuple
    lon_value, lat_value = l

    # Find indices using values directly
    idx = np.where(lon == lon_value)[0][0]
    idy = np.where(lat == lat_value)[0][0]

    print(f'Index for lon: {idx}, Index for lat: {idy}')
