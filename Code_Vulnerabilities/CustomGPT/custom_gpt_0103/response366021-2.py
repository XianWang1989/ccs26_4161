
import numpy as N
import itertools

# Sample lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Define lon and lat for the example
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1

for l in xy:
    b += 1
    # Access the tuple elements directly
    idx = N.where(lon == l[0])[0][0]  # l[0] accesses the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # l[1] accesses the second element of the tuple

    print(f"Index Lon: {idx}, Index Lat: {idy}")
