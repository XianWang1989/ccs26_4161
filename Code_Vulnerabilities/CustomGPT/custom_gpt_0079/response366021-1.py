
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a cartesian product of the lists
xy = list(itertools.product(lx, ly))

# Print to check the contents of xy
print(xy)  # should display combinations like [(3.625, 41.435), (3.625, 42.435), ...]

# Initialize indices
b = 0  # Start from 0
v = 1  # Fixed index since we need the second value

# Assuming lon and lat are defined earlier in your code as numpy arrays
lon = N.array([3.625, 4.625])  # Example lon values
lat = N.array([41.435, 42.435])  # Example lat values

for l in xy:
    idx = N.where(lon == l[0])[0][0]  # Access the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access the second element of the tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
