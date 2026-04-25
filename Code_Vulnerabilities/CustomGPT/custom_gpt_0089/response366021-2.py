
import numpy as N
import itertools

# Example data
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Assume lon and lat are Numpy arrays defined earlier
lon = N.array([3.625, 4.625, 5.0])  # Example longitude values
lat = N.array([41.435, 42.435, 43.0])  # Example latitude values

b = -1
v = 1

for l in xy:  # l is a tuple (longitude, latitude)
    b += 1
    # Access the elements of l directly
    idx = N.where(lon == l[0])[0][0]  # Using l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Using l[1] for latitude
    print(f"Indices: idx={idx}, idy={idy}")
