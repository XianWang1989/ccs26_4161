
import numpy as N
import itertools

# Sample lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create combinations
xy = list(itertools.product(lx, ly))

# Print the combinations for visualization
print(xy)

# Example latitude and longitude arrays
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Initialize indices
b = -1
v = 1

# Iterate over the combinations
for l in xy:
    b += 1
    # Instead of l[b][b], use l[0] and l[1]
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]
    print(f"Index in lon: {idx}, Index in lat: {idy}")
