
import numpy as N
import itertools

# Sample lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create combinations using itertools
xy = list(itertools.product(lx, ly))

b = -1
v = 1

for l in xy:
    b += 1
    # Use correct access for tuple elements
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]

    # You may add further processing here
