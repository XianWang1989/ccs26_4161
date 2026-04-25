
import numpy as N
import itertools

# Sample lists (assuming longer versions in your use case)
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # The lists are not the same size

xy = list(itertools.product(lx, ly))

# Print xy to see the structure
print(xy)  # Example: [(3.625, 41.435), (3.625, 42.435), ...]

# Initialize b and v
b = -1
v = 1

# Assume lon and lat are defined somewhere in your script
# Example arrays for demonstration
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

for l in xy:
    b += 1
    # Directly access the tuple values
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]

    # Example of what you might do with idx and idy
    print(f"Index in lon: {idx}, Index in lat: {idy}")
