
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]  # Example values
ly = [41.435, 42.435]  # Example values

# Create a Cartesian product of the lists
xy = list(itertools.product(lx, ly))

# Assuming lon and lat are your numpy arrays with latitude and longitude
lon = N.array([3.625, 4.625])  # Example lon values
lat = N.array([41.435, 42.435])  # Example lat values

b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access first element of l
    idy = N.where(lat == l[1])[0][0]  # Access second element of l
    print(f"Index for lon: {idx}, Index for lat: {idy}")
