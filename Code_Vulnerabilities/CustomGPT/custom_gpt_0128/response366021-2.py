
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

# Example lon and lat arrays
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1
for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access the first element directly
    idy = N.where(lat == l[1])[0][0]  # Access the second element directly
    print(f"Index lon: {idx}, Index lat: {idy}")
