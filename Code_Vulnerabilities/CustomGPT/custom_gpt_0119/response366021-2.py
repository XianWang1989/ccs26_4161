
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Assuming lon and lat are numpy arrays previously defined
lon = N.array([3.625, 4.625, 5.0])  # example lon values
lat = N.array([41.435, 42.435, 43.0])  # example lat values

b = -1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Corrected indexing
    idy = N.where(lat == l[1])[0][0]  # Corrected indexing
    print(f'Index in lon: {idx}, Index in lat: {idy}')
