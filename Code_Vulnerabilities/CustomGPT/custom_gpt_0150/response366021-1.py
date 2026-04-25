
import numpy as N
import itertools

# Sample data for demonstration
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a Cartesian product of the two lists
xy = list(itertools.product(lx, ly))

# Debugging output
print(xy)  # Should print the combinations

# Example coordinates for demonstration
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1
v = 1

for l in xy:
    b += 1  # Incrementing b for the index
    idx = N.where(lon == l[0])[0][0]  # Access using indices directly
    idy = N.where(lat == l[1])[0][0]  # Access using indices directly
    print(f"Index found at idx: {idx}, idy: {idy}")
