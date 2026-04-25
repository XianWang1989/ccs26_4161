
import numpy as N
import itertools

# Example data (replace with your actual data)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))  # Create pairs of (x, y)
print(xy)  # Check the Cartesian product

lon = N.array([3.625, 4.625])           # Dummy lon array
lat = N.array([41.435, 42.435])         # Dummy lat array

b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Use l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Use l[1] for latitude
    print(f"Index in lon: {idx}, Index in lat: {idy}")
