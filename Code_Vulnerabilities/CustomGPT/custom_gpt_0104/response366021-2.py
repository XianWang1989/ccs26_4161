
import numpy as N
import itertools

# Lists with example numbers.
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a "table" of the lists using itertools
xy = list(itertools.product(lx, ly))  # Will produce tuples like [(3.625, 41.435), (3.625, 42.435), ...]

# Sample output to check xy
print(xy)

# Initialize b and v
b = -1
v = 1

# Assume lon and lat are numpy arrays loaded earlier in the script
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

for l in xy:
    b += 1
    # Access the elements of the tuple l directly
    idx = N.where(lon == l[0])[0][0]  # Get lon from l[0]
    idy = N.where(lat == l[1])[0][0]  # Get lat from l[1]
    print(f'Index in lon: {idx}, Index in lat: {idy}')
