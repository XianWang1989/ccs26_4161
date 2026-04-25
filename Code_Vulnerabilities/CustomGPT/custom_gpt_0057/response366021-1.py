
import numpy as N
import itertools

lx = [3.625, 4.625]  # Sample data
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

b = -1
v = 1

lon = N.array([3.625, 4.625])  # Example latitudes for testing
lat = N.array([41.435, 42.435])  # Example longitudes for testing

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Accessing the first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Accessing the second element of tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
