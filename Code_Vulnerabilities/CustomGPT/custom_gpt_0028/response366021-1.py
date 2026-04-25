
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

# Create product of two lists
xy = list(itertools.product(lx, ly))

# Print the Cartesian product
print(xy)  # [(3.625, 41.435), (3.625, 42.435), ...]

# Assuming 'lon' and 'lat' are numpy arrays with float values
lon = N.array([3.625, 4.625])  # Example longitude array
lat = N.array([41.435, 42.435])  # Example latitude array

b = -1
for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Correctly accessing first element of tuple l
    idy = N.where(lat == l[1])[0][0]  # Correctly accessing second element of tuple l

    print(f'Index in lon: {idx}, Index in lat: {idy}')
