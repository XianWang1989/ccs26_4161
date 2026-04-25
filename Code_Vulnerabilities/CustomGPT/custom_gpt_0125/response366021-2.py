
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a product of the two lists
xy = list(itertools.product(lx, ly))

# Access using direct tuple indexing
for b, (x_val, y_val) in enumerate(xy):
    idx = N.where(lon == x_val)[0][0]
    idy = N.where(lat == y_val)[0][0]
