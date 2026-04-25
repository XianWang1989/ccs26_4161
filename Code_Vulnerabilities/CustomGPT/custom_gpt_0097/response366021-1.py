
import numpy as N
import itertools

# Create two lists of floats
lx = [3.625, 4.625]  # Example values
ly = [41.435, 42.435]  # Example values

xy = list(itertools.product(lx, ly))  # Create combinations of the lists

# Example lon and lat arrays
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access first value of tuple
    idy = N.where(lat == l[1])[0][0]  # Access second value of tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
