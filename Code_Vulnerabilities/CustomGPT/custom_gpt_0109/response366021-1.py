
import numpy as N
import itertools

# Sample lists for demonstration
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a product of lx and ly
xy = list(itertools.product(lx, ly))

# Assuming lon and lat are defined elsewhere
lon = N.array([3.625, 4.625])  # Example array for demonstration
lat = N.array([41.435, 42.435])  # Example array for demonstration

# Initialize b and v
b = 0  # Start from 0 to match the indexing of xy
v = 1

for l in xy:
    idx = N.where(lon == l[0])[0][0]  # Accessing the first element directly
    idy = N.where(lat == l[1])[0][0]  # Accessing the second element directly
    # Process idx and idy as needed
