
import numpy as N
import itertools

lx = [3.625, 4.625]  # Example data
ly = [41.435, 42.435]  # Example data

xy = list(itertools.product(lx, ly))

# Sample output for debugging
print(xy)  # [(3.625, 41.435), (3.625, 42.435), ...]

# Corrected loop
for l in xy:
    idx = N.where(lon == l[0])[0][0]  # Access the first element (longitude)
    idy = N.where(lat == l[1])[0][0]  # Access the second element (latitude)
