
import numpy as N
import itertools

lx = [3.625, 4.625]  # Example values
ly = [41.435, 42.435]  # Example values

# Create combinations
xy = list(itertools.product(lx, ly))
print(xy)  # Outputs tuples of (lx, ly)

# Assuming lon and lat are numpy arrays read earlier
lon = N.array([3.625, 4.625])  # Example lon values
lat = N.array([41.435, 42.435])  # Example lat values

# Corrected iteration
for l in xy:
    idx = N.where(lon == l[0])[0]  # Use l[0] for longitude
    idy = N.where(lat == l[1])[0]  # Use l[1] for latitude

    # Check if idx and idy are not empty
    if idx.size > 0 and idy.size > 0:
        print(f"Found indices: idx = {idx[0]}, idy = {idy[0]}")
    else:
        print("Coordinates not found in lat/lon.")
