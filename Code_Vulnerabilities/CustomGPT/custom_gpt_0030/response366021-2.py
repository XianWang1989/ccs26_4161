
import numpy as N
import itertools

# Sample data for testing
lx = [3.625, 4.625]
ly = [41.435, 42.435]
lon = N.array([3.625, 4.625, 3.645])  # Example longitude array
lat = N.array([41.435, 42.435, 41.450])  # Example latitude array

xy = list(itertools.product(lx, ly))

b = -1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Use l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Use l[1] for latitude
    print(f'Index for lon: {idx}, Index for lat: {idy}')  # Output indices
