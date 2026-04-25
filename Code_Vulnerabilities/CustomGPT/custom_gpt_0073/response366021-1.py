
import numpy as N
import itertools

# Sample lists with floats
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create a "table" of the lists
xy = list(itertools.product(lx, ly))

# Print the product
print(xy)  # [(3.625, 41.435), (3.625, 42.435), ...]

# Access values from xy
print(xy[0][0])  # This works
print(xy[0][1])  # This works

# Example lat/lon arrays (replace with your actual data)
lon = N.array([3.625, 3.625, 4.625])
lat = N.array([41.435, 42.435, 41.435])

# Initialize b and v
b = 0
v = 1

for l in xy:
    idx = N.where(lon == l[0])[0][0]  # Access first element
    idy = N.where(lat == l[1])[0][0]  # Access second element
    print(f"Index in lon: {idx}, Index in lat: {idy}")
