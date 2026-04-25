
import numpy as N
import itertools

# Sample lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

# Sample lon and lat arrays for demonstration
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Initialize b and v
b = 0  # Start from 0
v = 1  # Second index for accessing tuples

for l in xy:
    # Access values directly from the tuple
    idx = N.where(lon == l[0])[0][0]  # Use l[0] instead of l[b]
    idy = N.where(lat == l[1])[0][0]  # Use l[1] instead of l[v]

    print(f"Indices: idx={idx}, idy={idy}, Values: lon[{idx}]={lon[idx]}, lat[{idy}]={lat[idy]}")
