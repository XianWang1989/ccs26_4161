
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a Cartesian product of the lists
xy = list(itertools.product(lx, ly))

# Printing the Cartesian product
print(xy) 

# Initialize index values
b = -1  

# Assuming lon and lat are defined earlier
lon = N.array([3.625, 4.625])  # Sample lon array
lat = N.array([41.435, 42.435])  # Sample lat array

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of tuple

    print(f"Index in lon: {idx}, Index in lat: {idy}")
