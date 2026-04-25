
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]  # replace with your actual data
ly = [41.435, 42.435]  # replace with your actual data

# Create combinations of lists
xy = list(itertools.product(lx, ly))

# Example arrays for lon and lat
lon = N.array([3.625, 4.625, 5.0])  # Replace with your actual data
lat = N.array([41.435, 42.435, 43.0])  # Replace with your actual data

b = -1
v = 1

# Iterate over combinations
for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
