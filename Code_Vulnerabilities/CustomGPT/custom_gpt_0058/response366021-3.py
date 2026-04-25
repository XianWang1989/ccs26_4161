
import numpy as N
import itertools

# Example lists of coordinates 
lx = [3.625, 4.625]  # Replace with your actual values
ly = [41.435, 42.435]  # Replace with your actual values

# Generate the cartesian product
xy = list(itertools.product(lx, ly))

# Example lat/lon arrays
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Process the Cartesian product
b = -1
v = 1

for l in xy:
    b += 1
    idx = N.where(lon == l[0])[0][0]  # Access first value for longitude
    idy = N.where(lat == l[1])[0][0]  # Access second value for latitude
    print(f'Index for longitude {l[0]}: {idx}, Index for latitude {l[1]}: {idy}')
