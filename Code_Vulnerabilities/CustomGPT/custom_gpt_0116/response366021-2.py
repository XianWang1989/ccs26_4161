
import numpy as N
import itertools

# Example data
lx = [3.625, 4.625]  # Small example for brevity
ly = [41.435, 42.435]

# Create all combinations of lx and ly
xy = list(itertools.product(lx, ly))

# Assuming lon and lat are defined elsewhere
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1
v = 1

# Iterate over the tuples in xy
for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access first element of l
    idy = N.where(lat == l[1])[0][0]  # Access second element of l
    print(f"Index: {idx}, {idy}")
