
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a product of the two lists
xy = list(itertools.product(lx, ly))

# Print the generated tuples
print(xy)  # [(3.625, 41.435), (3.625, 42.435), ... ]

# Initialize b and v for indexing
b = -1  # Start at -1 for incrementing
v = 1   # The index to access the second element

# Assume lon and lat are defined previously
lon = N.array([3.625, 4.625])   # Example longitude array
lat = N.array([41.435, 42.435])  # Example latitude array

# Loop through the xy product
for l in xy:
    b += 1  # Increment b for the index

    # Access elements of l directly without using b
    lon_value = l[0]  # First element of the tuple
    lat_value = l[1]  # Second element of the tuple

    # Properly use N.where to find indices
    idx = N.where(lon == lon_value)[0][0]  # Get index for lon
    idy = N.where(lat == lat_value)[0][0]  # Get index for lat

    # Perform your operation here
    print(f"Index for lon: {idx}, Index for lat: {idy}")
