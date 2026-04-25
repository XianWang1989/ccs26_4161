
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # Adjust lists as needed

# Create a Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

b = -1
v = 1

# Iterate over the Cartesian product
for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access the second element of the tuple

    # Do something with idx and idy
