
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a Cartesian product of the lists
xy = list(itertools.product(lx, ly))

# Example latitude and longitude arrays (replace with your actual data)
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Iteration variables
b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Use l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Use l[1] for latitude
    print(f"Index for lon: {idx}, Index for lat: {idy}")
