
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]  # Replace with actual data
ly = [41.435, 42.435]  # Replace with actual data

# Create a product of lx and ly
xy = list(itertools.product(lx, ly))

print(xy)  # Output: [(3.625, 41.435), (3.625, 42.435), ...]

b = -1
v = 1

# Assuming lon and lat are numpy arrays
lon = N.array([3.625, 4.625, ...])  # Example for lon
lat = N.array([41.435, 42.435, ...])  # Example for lat

for l in xy:
    b += 1
    # Correctly access the elements of l
    idx = N.where(lon == l[0])[0][0]  # Use l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Use l[1] for latitude
