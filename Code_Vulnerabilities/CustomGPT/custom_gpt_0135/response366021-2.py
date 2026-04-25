
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # Example data

# Create a Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

# Example arrays for lon and lat
lon = N.array([3.625, 4.625])       # Example longitude array
lat = N.array([41.435, 42.435])      # Example latitude array

b = -1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access directly using l[0]
    idy = N.where(lat == l[1])[0][0]  # Access directly using l[1]
    print(f"Index of lon: {idx}, Index of lat: {idy}")
