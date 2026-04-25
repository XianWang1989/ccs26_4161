
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]  # replace ... with actual values
ly = [41.435, 42.435]  # replace ... with actual values

xy = list(itertools.product(lx, ly))  # create a "table" of the lists

# Let's simulate lon and lat arrays for demonstration
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access the first value of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access the second value of the tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
