
import numpy as N
import itertools

# Example lists of floating-point numbers
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

print(xy)  # Output: [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Initialize indices b and v
b = -1
v = 1

# Assuming lon and lat are defined as numpy arrays
lon = N.array([3.625, 4.625])       # Example value
lat = N.array([41.435, 42.435])     # Example value

# Loop through the tuples in xy
for l in xy:
    b += 1
    # Access the elements of the tuple directly
    idx = N.where(lon == l[0])[0][0]  # l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # l[1] for latitude
    print(f"Index in lon: {idx}, Index in lat: {idy}")
