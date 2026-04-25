
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]  # Example values
ly = [41.435, 42.435]  # Example values

# Create a Cartesian product
xy = list(itertools.product(lx, ly))

# Example lon and lat arrays
lon = N.array([3.625, 4.625])  # Replace with actual lon values
lat = N.array([41.435, 42.435])  # Replace with actual lat values

b = -1
for l in xy:
    b += 1
    # Accessing tuple elements directly
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]

    print(f"Index in lon: {idx}, Index in lat: {idy}")
