
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # Make sure they contain valid numbers

# Create Cartesian product
xy = list(itertools.product(lx, ly))

print(xy)  # [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Example longitude and latitude arrays
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1
v = 1

for l in xy:
    b += 1
    # Correct the indexing here
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]

    print(f"Index in lon: {idx}, Index in lat: {idy}")
