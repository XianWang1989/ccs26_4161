
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]  # Example values
ly = [41.435, 42.435]  # Example values

xy = list(itertools.product(lx, ly))  # Create combinations of lists

lon = N.array([3.625, 4.625])  # Example longitude values
lat = N.array([41.435, 42.435])  # Example latitude values

b = -1  # Initialize b
v = 1   # Initialize v

for l in xy:
    b += 1
    # Access elements directly from l
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]
    print(f"Index for lon: {idx}, Index for lat: {idy}")
