
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Assuming lon and lat are defined earlier as numpy arrays, e.g.:
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Starting point
for l in xy:
    # Use 0 and 1 as the indices directly
    idx = N.where(lon == l[0])[0][0]  # First element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Second element of the tuple

    print(f"Index in lon: {idx}, Index in lat: {idy}")
