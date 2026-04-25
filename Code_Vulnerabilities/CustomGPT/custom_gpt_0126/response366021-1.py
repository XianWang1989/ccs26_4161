
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]  # Example float values
ly = [41.435, 42.435]  # Example float values

# Create Cartesian product of the lists
xy = list(itertools.product(lx, ly))

# Assuming lon and lat are already defined as numpy arrays

# Example lon and lat for testing
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Iterating over the product
for l in xy:
    idx = N.where(lon == l[0])[0][0]  # Access first element of tuple l
    idy = N.where(lat == l[1])[0][0]  # Access second element of tuple l

    print(f"Index for lon: {idx}, Index for lat: {idy}")
