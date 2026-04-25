
import numpy as N
import itertools

# Create two lists, containing large amounts of numbers
lx = [3.625, 4.625]  # example values
ly = [41.435, 42.435]  # example values

# Create a Cartesian product of the two lists
xy = list(itertools.product(lx, ly))
print(xy)  # Outputs: [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Assuming lon and lat are previously defined numpy arrays of latitude and longitude
lon = N.array([3.625, 4.625])  # example values
lat = N.array([41.435, 42.435])  # example values

# Start indices at 0
for l in xy:
    # Directly refer to the elements of the tuple
    idx = N.where(lon == l[0])[0][0]  # Access the first element of the tuple
    idy = N.where(lat == l[1])[0][0]  # Access the second element of the tuple
    print(f'Index of lon: {idx}, Index of lat: {idy}')
