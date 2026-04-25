
import numpy as N
import itertools

# I created two lists, containing large amounts of numbers, i.e. 3.465
lx = [3.625, 4.625]  # Example values for illustration
ly = [41.435, 42.435]  # Example values for illustration

xy = list(itertools.product(lx, ly))  # create a nice "table" of my lists

# printed to show structure (uncomment in real usage)
# print(xy)  

# Assuming lon and lat are defined as numpy arrays somewhere in your code
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Initialize b and v directly representing the positions
for l in xy:
    idx = N.where(lon == l[0])[0][0]  # l[0] corresponds to the first element in the tuple
    idy = N.where(lat == l[1])[0][0]  # l[1] corresponds to the second element in the tuple
    print(f'Index in lon: {idx}, Index in lat: {idy}')  # For verification, to show indices found
