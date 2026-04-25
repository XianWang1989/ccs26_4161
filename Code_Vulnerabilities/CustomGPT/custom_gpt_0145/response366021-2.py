
import numpy as N
import itertools

# Example lists, replace these with your actual data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a Cartesian product of lx and ly
xy = list(itertools.product(lx, ly)) 

# Print xy for debugging
print(xy)

# Initialize b and v
b = -1
v = 1

# Make sure lon and lat are defined here as Numpy arrays
lon = N.array([3.625, 4.625])  # Example data
lat = N.array([41.435, 42.435]) # Example data

# Iterate through tuples in xy
for l in xy:
    b += 1
    # Access elements correctly using fixed indices
    idx = N.where(lon == l[0])[0][0]  # l[0] accesses the first element
    idy = N.where(lat == l[1])[0][0]  # l[1] accesses the second element
    print(f"Index in lon: {idx}, Index in lat: {idy}")
