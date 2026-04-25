
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]  # Add your full list here
ly = [41.435, 42.435]  # Add your full list here

xy = list(itertools.product(lx, ly))  # Create a "table" of pairs

print(xy)  # Example output: [(3.625, 41.435), (3.625, 42.435), ...]

# Initialize longitude and latitude arrays
lon = N.array([3.625, 4.625, ...])  # Your actual longitude values
lat = N.array([41.435, 42.435, ...])  # Your actual latitude values

b = -1
v = 1

for l in xy:
    b += 1
    # Directly access l[0] and l[1] instead of indexing with b
    idx = N.where(lon == l[0])[0][0]  # Access longitude
    idy = N.where(lat == l[1])[0][0]  # Access latitude
