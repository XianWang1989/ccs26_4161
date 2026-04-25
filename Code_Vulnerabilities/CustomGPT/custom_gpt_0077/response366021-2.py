
import numpy as N
import itertools

# Example input lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create the cartesian product
xy = list(itertools.product(lx, ly))

# Example longitude and latitude arrays
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Iterate over the cartesian product
for l in xy:
    # Directly access the values from the tuple
    idx = N.where(lon == l[0])[0][0]  # Access first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of the tuple

    # Output the indices
    print(f'Index in lon: {idx}, Index in lat: {idy}')
