
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]  # Add more values as necessary
ly = [41.435, 42.435]  # Add more values as necessary

# Creating a Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

# Sample lon and lat arrays
lon = N.array([3.625, 4.625, 5.0])
lat = N.array([41.435, 42.435, 43.0])

b = -1

for l in xy:
    b += 1
    lon_value = l[0]  # Correctly access the first value
    lat_value = l[1]  # Correctly access the second value

    idx = N.where(lon == lon_value)[0][0]
    idy = N.where(lat == lat_value)[0][0]

    print(f"Index of lon: {idx}, Index of lat: {idy}")
