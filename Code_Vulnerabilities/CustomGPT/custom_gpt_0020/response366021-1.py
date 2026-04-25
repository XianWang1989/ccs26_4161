
import numpy as N
import itertools

# Assuming lx and ly are defined properly
lx = [3.625, 4.625] # Sample values
ly = [41.435, 42.435] # Sample values

xy = list(itertools.product(lx, ly)) # Create a "table" of my lists

print(xy) 
# This will print something like:
# [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# down here is where the error occurs
# Sample lat/lon arrays for demonstration
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1
v = 1

for l in xy:
    b += 1
    # Accessing elements directly without using b as an index for l
    lon_value = l[0]  # First element of the tuple
    lat_value = l[1]  # Second element of the tuple

    idx = N.where(lon == lon_value)[0][0]
    idy = N.where(lat == lat_value)[0][0]

    print(f"Index for lon {lon_value}: {idx}, Index for lat {lat_value}: {idy}")
