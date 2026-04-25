
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]  # Ensure the lists are complete
ly = [41.435, 42.435]

# Create the Cartesian product of lx and ly
xy = list(itertools.product(lx, ly))

lon = N.array([3.625, 4.625])  # Example longitude array
lat = N.array([41.435, 42.435])  # Example latitude array

b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access first value in tuple
    idy = N.where(lat == l[1])[0][0]  # Access second value in tuple

    # Example output
    print(f"Index in lon: {idx}, Index in lat: {idy}")
