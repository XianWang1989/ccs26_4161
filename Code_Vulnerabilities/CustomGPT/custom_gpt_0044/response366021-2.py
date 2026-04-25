
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]  # Example numbers
ly = [41.435, 42.435]

# Create a Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

# Assuming lon and lat are defined earlier in your code
lon = N.array([3.625, 4.625, ...])  # Replace with your actual array
lat = N.array([41.435, 42.435, ...])  # Replace with your actual array

b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access the first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Access the second element of tuple

    # Further processing can go here
