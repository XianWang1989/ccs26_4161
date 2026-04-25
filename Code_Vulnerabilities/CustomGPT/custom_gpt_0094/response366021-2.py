
import numpy as N
import itertools

# Sample data for demonstration
lx = [3.625, 4.625]
ly = [41.435, 42.435]
lon = N.array([3.625, 4.625])  # Example latitude values
lat = N.array([41.435, 42.435])  # Example longitude values

xy = list(itertools.product(lx, ly))

# Iterate directly over the tuples in xy
for l in xy:
    # Directly unpack the tuple l
    lon_value, lat_value = l

    # Use the unpacked values to find indices
    idx = N.where(lon == lon_value)[0][0]
    idy = N.where(lat == lat_value)[0][0]

    print(f"Indices: idx={idx}, idy={idy}")
