
import numpy as N
import itertools

# Sample lists to illustrate the issue
lx = [3.625, 4.625]  # Example numbers
ly = [41.435, 42.435]  # Example numbers

xy = list(itertools.product(lx, ly))

print(xy)  # Outputs: [(3.625, 41.435), (3.625, 42.435), ...]

# Initial indices
b = -1
v = 1

# Assuming lon and lat are defined elsewhere and are NumPy arrays
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

for l in xy:
    b += 1
    # Directly use indexing without using variable b
    idx = N.where(lon == l[0])[0][0]  # Access only the first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Access only the second element of tuple
    print(f'Index in lon: {idx}, Index in lat: {idy}')  # Optional debug print
