
import numpy as N
import itertools

# Example lists
lx = [3.625, 4.625]
ly = [41.435, 42.435]  # Example shortened lists

xy = list(itertools.product(lx, ly))  # Create a cartesian product of the lists

# Assuming lon and lat are defined earlier correctly
lon = N.array([3.625, 4.625])
lat = N.array([41.435, 42.435])

# Initialize b and v
b = -1
v = 1

for l in xy:
    b += 1
    # Access elements directly using l[0] and l[1]
    idx = N.where(lon == l[0])[0][0]  # Use l[0] for longitude
    idy = N.where(lat == l[1])[0][0]  # Use l[1] for latitude
    print(f"Index in lon: {idx}, Index in lat: {idy}")  # Add your desired operations here
