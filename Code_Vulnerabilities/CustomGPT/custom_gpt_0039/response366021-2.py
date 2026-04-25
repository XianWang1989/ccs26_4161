
import numpy as N
import itertools

# Example data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

lon = N.array([3.625, 4.625])  # Example longitude array
lat = N.array([41.435, 42.435]) # Example latitude array

b = -1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Accessing first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Accessing second element of tuple
    print(f"Index: {idx}, {idy}")  # Print indices for verification
