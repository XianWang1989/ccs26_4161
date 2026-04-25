
import numpy as N
import itertools

# Sample list of floats
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create Cartesian product
xy = list(itertools.product(lx, ly))

# Print the Cartesian product
print(xy) 
# Output: [(3.625, 41.435), (3.625, 42.435), ...]

# Initialize indices
b = -1
v = 1

# Assuming lon and lat are numpy arrays with the required values
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

for l in xy:
    b += 1
    # Get specific values from the tuple `l`
    lon_value = l[0]  # Access first element of the tuple
    lat_value = l[1]  # Access second element of the tuple

    # Find indices using these values
    idx = N.where(lon == lon_value)[0][0]
    idy = N.where(lat == lat_value)[0][0]

    print(f"Indices for {lon_value}, {lat_value}: ({idx}, {idy})")
