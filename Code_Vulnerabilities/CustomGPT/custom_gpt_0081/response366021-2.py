
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create Cartesian product
xy = list(itertools.product(lx, ly))  # [(3.625, 41.435), (3.625, 42.435)]

# Sample longitude and latitude arrays, replace with your actual arrays
lon = N.array([3.625, 4.625])  # Example longitude array
lat = N.array([41.435, 42.435])  # Example latitude array

# Initialize index
b = -1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access l[0] for the longitude
    idy = N.where(lat == l[1])[0][0]  # Access l[1] for the latitude

    print(f"Index in lon: {idx}, Index in lat: {idy}")
