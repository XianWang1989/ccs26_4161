
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a product of the lists
xy = list(itertools.product(lx, ly))

# Assuming lon and lat are numpy arrays defined earlier
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Initialize b and v
b = -1
v = 1

for l in xy:
    b += 1  # Keep track of index (not actually needed for accessing 'l')
    idx = N.where(lon == l[0])[0][0]  # Access the first element of tuple l
    idy = N.where(lat == l[1])[0][0]  # Access the second element of tuple l

    # Example print statements for debugging
    print("Index in lon:", idx)
    print("Index in lat:", idy)
