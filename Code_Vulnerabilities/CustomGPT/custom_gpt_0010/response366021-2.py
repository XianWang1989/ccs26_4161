
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # The lists can have different sizes

xy = list(itertools.product(lx, ly))  # create pairs of (x, y)

# Assume lon and lat are defined as numpy arrays. Here's an example:
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1
# Updated for loop
for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access the second element of the tuple
