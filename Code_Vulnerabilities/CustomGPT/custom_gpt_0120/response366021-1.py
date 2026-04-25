
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create product of both lists
xy = list(itertools.product(lx, ly))

# Initialize variables for accessing longitude/latitude
lon = N.array([3.625, 4.625])  # Example longitude array
lat = N.array([41.435, 42.435]) # Example latitude array

b = -1
v = 1

# Loop through the pairs in xy
for l in xy:
    b += 1
    # Accessing elements correctly
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]
    print(f"Index for lon: {idx}, Index for lat: {idy}")
