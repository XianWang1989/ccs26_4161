
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create Cartesian product
xy = list(itertools.product(lx, ly))

# Assuming lon and lat are numpy arrays
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

for l in xy:
    # Directly access values from the tuple
    lon_value = l[0]
    lat_value = l[1]

    # Using where to find indices
    idx = N.where(lon == lon_value)[0][0]
    idy = N.where(lat == lat_value)[0][0]

    print(f"Index for lon {lon_value}: {idx}, Index for lat {lat_value}: {idy}")
