
import numpy as N
import itertools

# Sample lists (replace these with actual values)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a Cartesian product of the two lists
xy = list(itertools.product(lx, ly))

print(xy) # Check the content of xy

# Initialize b and v for indexing
b = -1
v = 1

# Assuming lon and lat are numpy arrays defined earlier
# Example latitude/longitude arrays (replace with actual data)
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

for l in xy:
    b += 1
    # Accessing the values from the tuple l directly
    idx = N.where(lon == l[0])[0][0]  # Accessing the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Accessing the second element of the tuple
    # You can add further processing here
