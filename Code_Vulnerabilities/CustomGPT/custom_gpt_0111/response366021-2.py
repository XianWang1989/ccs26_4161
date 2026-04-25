
import numpy as N
import itertools

lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Sample lon and lat arrays for demonstration
lon = N.array([3.625, 4.625])  # Replace this with your actual latitudes
lat = N.array([41.435, 42.435]) # Replace this with your actual longitudes

b = -1
for l in xy:
    b += 1
    # Access l directly: l[0] for longitude and l[1] for latitude
    idx = N.where(lon == l[0])[0][0]  # Use l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Use l[1] for latitude
