
import numpy as N
import itertools

# Assuming lx and ly are defined as before
lx = [3.625, 4.625, ...]
ly = [41.435, 42.435, ...]  # The lists are not the same size!

xy = list(itertools.product(lx, ly))

b = -1
for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Accessing the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Accessing the second element of the tuple
