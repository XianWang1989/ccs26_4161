
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Assume lon and lat are defined as follows
lon = N.array([3.625, 4.625])  # Example longitude values
lat = N.array([41.435, 42.435])  # Example latitude values

b = -1
v = 1

for l in xy:
    b += 1
    # Access the float values directly from l
    idx = N.where(lon == l[0])[0][0]  # Use l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Use l[1] for latitude
    print(f"Index in lon: {idx}, Index in lat: {idy}")
