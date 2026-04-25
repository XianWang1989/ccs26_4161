
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # Example data

# Create a cartesian product of the lists
xy = list(itertools.product(lx, ly))

# Printing for verification
print(xy)

# Initialize b and v
b = -1
v = 1

# Assuming lon and lat are defined earlier
lon = N.array([3.625, 4.625])  # Example longitude array
lat = N.array([41.435, 42.435])  # Example latitude array

for l in xy:
    b += 1
    # Access l directly as a tuple
    idx = N.where(lon == l[0])[0][0]  # Use l[0] for lon
    idy = N.where(lat == l[1])[0][0]  # Use l[1] for lat

    print(f"Longitude index: {idx}, Latitude index: {idy}")
