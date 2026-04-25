
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Assume lon and lat arrays are defined
lon = N.array([3.625, 4.625, 3.5, 4.0])
lat = N.array([41.435, 42.435, 41.0])

b = -1
v = 1

for l in xy:
    b += 1
    # Access elements directly
    idx = N.where(lon == l[0])[0][0]  # l[0] is the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # l[1] is the second element of the tuple

    print("Index in lon:", idx, "Index in lat:", idy)
