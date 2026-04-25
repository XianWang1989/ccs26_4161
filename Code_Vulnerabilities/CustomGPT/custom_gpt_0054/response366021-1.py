
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]  # Add more as needed
ly = [41.435, 42.435]  # Add more as needed

# Create a product of both lists
xy = list(itertools.product(lx, ly))

# Assume lon and lat are defined and are NumPy arrays
lon = N.array([3.625, 4.625, 3.5])  # Example lon values
lat = N.array([41.435, 42.435, 41.5])  # Example lat values

# Initialize indices
for l in xy:
    # "l" is a tuple, so directly access elements without using "b"
    idx = N.where(lon == l[0])[0][0]  # Access first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of the tuple
    print("Index in lon:", idx, "Index in lat:", idy)
