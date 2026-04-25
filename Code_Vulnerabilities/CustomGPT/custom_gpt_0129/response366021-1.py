
import numpy as N
import itertools

# Sample lists for demonstration
lx = [3.625, 4.625]  # Complete the lists with more data
ly = [41.435, 42.435]  # Complete with more data

# Create a Cartesian product of the two lists
xy = list(itertools.product(lx, ly))

b = -1
v = 1

# Assuming lon and lat are defined elsewhere in your script
# For example:
lon = N.array([3.625, 4.625])  # Sample lon array
lat = N.array([41.435, 42.435])  # Sample lat array 

for l in xy:
    b += 1
    # Directly access the tuple elements
    idx = N.where(lon == l[0])[0][0]  # Access the first element directly
    idy = N.where(lat == l[1])[0][0]  # Access the second element directly

    print(f"Index in lon: {idx}, Index in lat: {idy}")
