
import numpy as np
import itertools

# Sample data for demonstration
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

# Example lon and lat arrays (these should be defined earlier in your code)
lon = np.array([3.625, 4.625])
lat = np.array([41.435, 42.435])

# Process the values
for l in xy:
    # Directly unpack l into its components
    lon_val, lat_val = l

    idx = np.where(lon == lon_val)[0][0]
    idy = np.where(lat == lat_val)[0][0]

    print(f"Index in lon: {idx}, Index in lat: {idy}")
