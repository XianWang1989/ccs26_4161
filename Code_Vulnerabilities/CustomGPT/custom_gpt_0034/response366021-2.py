
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]  

# Create a Cartesian product of the two lists
xy = list(itertools.product(lx, ly))

# Print the Cartesian product
print(xy)  # Output: [(3.625, 41.435), (3.625, 42.435), ...]

# Initialize b and v
b = -1
v = 1

# Assuming lon and lat are numpy arrays:
lon = N.array([3.625, 3.700, 4.625])
lat = N.array([41.435, 41.500, 42.435])

for l in xy:
    b += 1
    # Access the values directly from the tuple l
    idx = N.where(lon == l[0])[0][0]  # Use l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Use l[1] for latitude
    print(f"Index for lon: {idx}, Index for lat: {idy}")
