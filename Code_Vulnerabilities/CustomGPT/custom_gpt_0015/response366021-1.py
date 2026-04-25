
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Example latitude and longitude arrays
lon = N.array([3.625, 4.625])  # Example data
lat = N.array([41.435, 42.435])  # Example data

b = -1
v = 1

for l in xy:
    b += 1
    # Accessing values from the tuple directly
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]

    # Print for debugging
    print(f"Longitude index: {idx}, Latitude index: {idy}")
