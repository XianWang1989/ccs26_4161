
import numpy as N
import itertools

# Example data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Assuming lon and lat are numpy arrays defined earlier in your code
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1

for l in xy:
    b += 1
    # Use correct indexing for l which is a tuple, with indices directly
    idx = N.where(lon == l[0])[0][0]  # l[0] for the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # l[1] for the second element of the tuple
