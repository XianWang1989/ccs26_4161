
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Creating a product of the two lists
xy = list(itertools.product(lx, ly))

# Example longitude and latitude arrays
lon = N.array([3.625, 4.625, 3.5])
lat = N.array([41.435, 42.435, 41.5])

# Iterating through the product
for b, l in enumerate(xy):
    idx = N.where(lon == l[0])[0][0]  # Accessing the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Accessing the second element of the tuple
    print(f'Index in lon: {idx}, Index in lat: {idy}')
