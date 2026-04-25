
import numpy as np
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a product of the two lists
xy = list(itertools.product(lx, ly))

# Print xy
print(xy) 
# Output: [(3.625, 41.435), (3.625, 42.435), ...]

# Iterate over 'xy'
b = -1
v = 1

# Assume lon and lat are defined earlier
lon = np.array([3.625, 3.9, 4.625])
lat = np.array([41.435, 41.7, 42.435])

for l in xy:
    b += 1
    # Access the values directly from the tuple `l`
    idx = np.where(lon == l[0])[0][0]  # l[0] for longitude
    idy = np.where(lat == l[1])[0][0]  # l[1] for latitude
    print(f"Index for lon: {idx}, Index for lat: {idy}")
