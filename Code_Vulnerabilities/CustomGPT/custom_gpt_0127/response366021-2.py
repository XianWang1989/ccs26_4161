
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# The revised loop
for l in xy:
    idx = N.where(lon == l[0])[0][0]  # Accessing first element
    idy = N.where(lat == l[1])[0][0]  # Accessing second element
