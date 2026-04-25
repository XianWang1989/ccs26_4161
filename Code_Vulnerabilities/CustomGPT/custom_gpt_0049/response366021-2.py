
import numpy as N
import itertools

lx = [3.625, 4.625, ...]
ly = [41.435, 42.435, ...] 

xy = list(itertools.product(lx, ly))

# Assuming lon and lat are defined properly before this
for l in xy:
    idx = N.where(lon == l[0])[0][0]  # access first element
    idy = N.where(lat == l[1])[0][0]  # access second element
