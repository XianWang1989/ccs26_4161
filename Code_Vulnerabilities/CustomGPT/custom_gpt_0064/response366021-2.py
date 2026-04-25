
import numpy as N
import itertools

# Example data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create the Cartesian product
xy = list(itertools.product(lx, ly))

# Printing for debugging
print(xy)  # Example output: [(3.625, 41.435), (3.625, 42.435)]

b = -1
v = 1

for l in xy:
    b += 1
    # Correct indexing
    idx = N.where(lon == l[0])[0][0]  # Using l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Using l[1] for latitude
