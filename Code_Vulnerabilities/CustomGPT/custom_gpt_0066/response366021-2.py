
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]  # Example values
ly = [41.435, 42.435]  # Example values

xy = list(itertools.product(lx, ly))

# Debug print to check xy
print(xy)

# Assume lon and lat are defined as numpy arrays
lon = N.array([3.625, 4.625])  # Example longitude array
lat = N.array([41.435, 42.435])  # Example latitude array

b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Accessing l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Accessing l[1] for latitude

    # Example of what you might do next
    print(f'Index Lon: {idx}, Index Lat: {idy}')
