
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]  # Replace with your actual data
ly = [41.435, 42.435]  # Replace with your actual data

# Create a Cartesian product of the lists
xy = list(itertools.product(lx, ly))

# Sample lon and lat arrays for demonstration purposes
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Iterate over the products without needing an index variable
for l in xy:
    idx = N.where(lon == l[0])[0][0]
    idy = N.where(lat == l[1])[0][0]
    print(f'Index for longitude {l[0]}: {idx}, Index for latitude {l[1]}: {idy}')
