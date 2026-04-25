
import numpy as N
import itertools

# Assume lx and ly are defined as follows
lx = [3.625, 4.625]  # Example values
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Now access lat/lon correctly
lon = N.array([3.625, 4.625])   # Example array of longitudes
lat = N.array([41.435, 42.435])  # Example array of latitudes

b = -1
for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access the first value directly
    idy = N.where(lat == l[1])[0][0]  # Access the second value directly

    # Proceed with your processing...
