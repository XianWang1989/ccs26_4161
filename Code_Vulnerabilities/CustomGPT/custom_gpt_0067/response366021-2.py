
import numpy as N
import itertools

# Example lists (replace with your actual data)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Assuming lon and lat are defined earlier in your code
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Accessing first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Accessing second element of tuple
    print(f"Index: {idx}, {idy}")
