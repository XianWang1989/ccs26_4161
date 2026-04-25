
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

# Sample lon and lat arrays (for demonstration)
lon = N.array([3.625, 4.625, 5.625])
lat = N.array([41.435, 42.435, 43.435])

b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Accessing the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Accessing the second element of the tuple
    print(f'Index in lon: {idx}, Index in lat: {idy}')
