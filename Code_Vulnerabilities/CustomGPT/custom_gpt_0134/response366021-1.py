
import numpy as N
import itertools

lx = [3.625, 4.625, 5.625]  # Example values
ly = [41.435, 42.435, 43.435]  # Example values

xy = list(itertools.product(lx, ly))

lon = N.array([3.625, 4.625, 5.625])  # Example longitude array
lat = N.array([41.435, 42.435, 43.435])  # Example latitude array

b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access first element of tuple
    idy = N.where(lat == l[1])[0][0]  # Access second element of tuple
    print(f"Index in lon: {idx}, Index in lat: {idy}")
