
import numpy as N
import itertools

# Example data
lx = [3.625, 4.625]  # example data
ly = [41.435, 42.435]  # example data
lon = N.array([3.625, 3.700, 4.625])  # example longitude array
lat = N.array([41.435, 41.500, 42.435])  # example latitude array

xy = list(itertools.product(lx, ly))

print(xy)  # Just to see the output

b = -1
v = 1

for l in xy:
    b += 1
    # Use l[0] and l[1] directly instead of l[b][b] and l[b][v]
    idx = N.where(lon == l[0])[0][0]  # Access the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access the second element of the tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
