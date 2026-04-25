
import numpy as N
import itertools

# Sample data for lx and ly
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Example latitude/longitude arrays
lon = N.array([3.625, 4.625, 5.625])
lat = N.array([41.435, 42.435, 43.435])

b = -1
v = 1

for l in xy:
    b += 1
    # Accessing values directly from the tuple without indexing
    lon_value = l[0]
    lat_value = l[1]

    idx = N.where(lon == lon_value)[0][0]
    idy = N.where(lat == lat_value)[0][0]

    print(f"Index in lon: {idx}, Index in lat: {idy}")
