
import numpy as N
import itertools

# Sample lists
lx = [3.625, 4.625]  # Shortened for example
ly = [41.435, 42.435]

# Create the Cartesian product
xy = list(itertools.product(lx, ly))

# Simulated lon and lat arrays for demonstration
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Iterate through the product
for l in xy:
    idx = N.where(lon == l[0])[0][0]  # No need for b
    idy = N.where(lat == l[1])[0][0]  # No need for v

    # Here you can do something with idx and idy
    print(f"Index in lon: {idx}, Index in lat: {idy}")
