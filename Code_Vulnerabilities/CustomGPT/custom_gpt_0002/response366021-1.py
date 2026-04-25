
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435] # The lists should be same size for demonstration

xy = list(itertools.product(lx, ly)) # Create a nice "table" of my lists

# This will work correctly
print(xy) 
print(xy[0][0])
print(xy[0][1])

# Assume lon and lat are defined earlier
lon = N.array([3.625, 4.625, 4.725])  # Example longitude array
lat = N.array([41.435, 42.435, 42.535]) # Example latitude array

# Correction starts here
b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Accessing tuple elements directly
    idy = N.where(lat == l[1])[0][0]  # Accessing tuple elements directly
    print(f"Index longitude: {idx}, Index latitude: {idy}")
