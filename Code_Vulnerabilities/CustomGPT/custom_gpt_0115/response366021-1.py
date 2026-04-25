
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]  # Example values
ly = [41.435, 42.435]  # Example values

# Create combinations of lists
xy = list(itertools.product(lx, ly))

# Example lon and lat arrays for demonstration
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Iterate through combinations
for l in xy:
    # Unpack the tuple directly
    lon_value, lat_value = l

    # Find indices for lon and lat
    idx = N.where(lon == lon_value)[0][0]
    idy = N.where(lat == lat_value)[0][0]

    print(f'Index in lon: {idx}, Index in lat: {idy}')
