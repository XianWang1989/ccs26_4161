
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))  # Create a table of lists

# Print xy to verify
print(xy)  # [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Initialize indices
b = -1
v = 1

# Assuming lon and lat are defined as numpy arrays earlier in your code
# Example:
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

for l in xy:
    b += 1
    # Accessing directly from the tuple l
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]

    print(f"Index in lon: {idx}, Index in lat: {idy}")
