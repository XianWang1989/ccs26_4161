
import numpy as N
import itertools

lx = [3.625, 4.625]  # Example values
ly = [41.435, 42.435]  # Example values

xy = list(itertools.product(lx, ly))  # Create Cartesian product

# Example output
print(xy)  # Should print: [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Initialize index variable
b = -1

# Example arrays for lon and lat (replace with actual arrays)
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
