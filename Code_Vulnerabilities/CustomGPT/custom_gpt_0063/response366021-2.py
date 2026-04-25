
import numpy as N
import itertools

# Sample lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # The lists are not the same size

# Create a cartesian product of the lists
xy = list(itertools.product(lx, ly))

print(xy)
# Example output: [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Example lon/lat arrays (replace with your actual data)
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = 0
for l in xy:
    idx = N.where(lon == l[0])[0][0]  # Access first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
