
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Assuming lon and lat are numpy arrays previously defined
lon = N.array([3.625, 4.625])  # Example values
lat = N.array([41.435, 42.435])  # Example values

b = -1
v = 1

for l in xy:
    b += 1
    # Access l directly as a tuple
    idx = N.where(lon == l[0])[0][0]  # l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # l[1] for latitude

    print(f"Processed index: idx={idx}, idy={idy}")
