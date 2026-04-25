
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]

xy = list(itertools.product(lx, ly))

# Assuming lon and lat are defined and match the dimensions of your data
lon = N.array([...])  # Replace with your actual longitude data
lat = N.array([...])  # Replace with your actual latitude data

for l in xy:
    idx = N.where(lon == l[0])[0][0]  # Access using index 0
    idy = N.where(lat == l[1])[0][0]  # Access using index 1
