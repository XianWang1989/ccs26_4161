
import numpy as N
import itertools

# Sample lists (replace with your own data)
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create all combinations of lx and ly
xy = list(itertools.product(lx, ly))

# Example lon and lat arrays (replace these with your own data)
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1

for l in xy:
    b += 1
    # Corrected the accessing of l using fixed indices 0 and 1
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]

    # Debug prints to show the indices found
    print(f"Index for lon: {idx}, Index for lat: {idy}")
