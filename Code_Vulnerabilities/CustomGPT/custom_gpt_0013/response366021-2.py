
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # Let's use two elements for simplicity

xy = list(itertools.product(lx, ly))

# Simulated lon and lat arrays for demonstration
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1
for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Accessing first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Accessing second element of tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
