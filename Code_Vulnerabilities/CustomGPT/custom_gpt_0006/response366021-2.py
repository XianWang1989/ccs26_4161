
import numpy as N
import itertools

# Sample lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # Example values

xy = list(itertools.product(lx, ly))  # Create a combination of points

# Output of xy for debugging
print(xy) 
# [(3.625, 41.435), (3.625, 42.435), (4.625, 41.435), (4.625, 42.435)]

# Initialize b and v
b = 0  # Start from 0
v = 1  # Index for the second element

# Assuming lon and lat are numpy arrays with coordinates
lon = N.array([3.625, 4.625])  # Example lon array
lat = N.array([41.435, 42.435])  # Example lat array

for l in xy:
    idx = N.where(lon == l[0])[0][0]  # Correctly index into l
    idy = N.where(lat == l[1])[0][0]  # Correctly index into l

    print(f"Longitude index: {idx}, Latitude index: {idy}")
