
import numpy as N
import itertools

# Sample data
lx = [3.625, 4.625]  # Example data
ly = [41.435, 42.435]  # Example data
lon = N.array([3.625, 4.625, 5.625])  # Your longitude data
lat = N.array([41.435, 42.435, 43.435])  # Your latitude data

xy = list(itertools.product(lx, ly))

# Looping through xy
for l in xy:
    # l is now a tuple like (3.625, 41.435)
    idx = N.where(lon == l[0])[0][0]  # Accessing first element
    idy = N.where(lat == l[1])[0][0]  # Accessing second element

    # Do something with idx and idy
    print(f'Index in lon: {idx}, Index in lat: {idy}')
