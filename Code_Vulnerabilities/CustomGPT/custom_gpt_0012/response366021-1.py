
import numpy as N
import itertools

# Example lists for demonstration
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create combinations of lx and ly
xy = list(itertools.product(lx, ly)) 

print(xy)  # Print out paired values

# Assuming lon and lat arrays are previously defined numpy arrays
lon = N.array([3.625, 4.625, 3.500])
lat = N.array([41.435, 42.435, 41.500])

for l in xy:
    # Directly use l[0] and l[1] to access tuple values
    idx = N.where(lon == l[0])[0][0]  # access first value in the tuple
    idy = N.where(lat == l[1])[0][0]  # access second value in the tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
