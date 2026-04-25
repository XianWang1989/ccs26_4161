
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Print to check the values in xy
print(xy)  # [(3.625, 41.435), (3.625, 42.435), ...]

# Initialize indices
b = 0  # Start at 0
v = 1  # The index for the second element of the tuple

for l in xy:
    idx = N.where(lon == l[b])[0][0]  # Access the first element of tuple directly
    idy = N.where(lat == l[v])[0][0]  # Access the second element of tuple directly
    b += 1
