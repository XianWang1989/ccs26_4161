
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]  # Example list. Extend with actual values.
ly = [41.435, 42.435]  # Example list. Extend with actual values.

# Create a product of the lists
xy = list(itertools.product(lx, ly))

# Initialize some example longitude/latitude arrays
lon = N.array([3.625, 4.625])  # Example array. Replace with actual data.
lat = N.array([41.435, 42.435])  # Example array. Replace with actual data.

b = -1
v = 1

for l in xy:
    b += 1
    # Directly use l[0] and l[1] since l is a tuple
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]
    print(f'Index in lon: {idx}, Index in lat: {idy}')
