
import numpy as N
import itertools

# Sample lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create Cartesian product
xy = list(itertools.product(lx, ly))

# Example coordinates from lon/lat arrays (you should define these properly in your code)
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Initialize indices
b = -1

for l in xy:
    b += 1
    # Access l directly, since l is already a tuple
    idx = N.where(lon == l[0])[0][0]  # Access first element of the tuple for longitude
    idy = N.where(lat == l[1])[0][0]  # Access second element of the tuple for latitude

# Output the indices
print(f"Longitude Index: {idx}, Latitude Index: {idy}")
