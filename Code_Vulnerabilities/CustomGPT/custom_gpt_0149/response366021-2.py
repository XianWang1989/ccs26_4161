
import numpy as N
import itertools

lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

b = -1
v = 1

for l in xy:
    b += 1
    # Directly access elements of the tuple `l`
    idx = N.where(lon == l[0])[0][0]  # Accessing the first element
    idy = N.where(lat == l[1])[0][0]  # Accessing the second element
